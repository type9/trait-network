import operator, collections

from dependencies.dictogram import Dictogram

class Trait(Dictogram):
    def __init__(self, name):
        super(Trait, self).__init__()
        self.name = name

    def children(self):
        return self.keys()
    
    def sort(self):
        self = sorted(self.items(), key=lambda x: x[1], reverse=True)

    def walk(self, n):
        '''returns the nth node it is associated to'''
        return list(self.items())[n][1]

class TraitNetwork():
    '''This class accepts a list of object dictionaries in the following format:
        {'name': '<obj_name>' 
        'traits': {
            '<unique_trait_name>': 0.5,
            '<unique_trait_name>': 0.25,
            '<unique_trait_name>': 0.25
            }
        } 
        trait values should represent the weighting of how much it composes of each object adding up to 1.0'''
    def __init__(self, objects, sorted=False, reverse_association=False):
        # generation variables
        self.nodes = {}
        self.objects = objects

        self.sorted_lists = {}

        self.reverse_association = {} # stores the association of traits to objects
        self.reverse_association_bool = reverse_association

        # initialization
        self.generate_nodes(objects)

        if sorted:
            self.sort_nodes()

    def create_node(self, name):
        return Trait(name)

    def calc_association(self, object_traits, trait_1, trait_2):
        '''This method will return an association value based off of a predetermined formula'''
        association = float()
        association = (object_traits[trait_1] + object_traits[trait_2])/2
        return association

    def subtract_sets(self, list_1, list_2):
        if list_2 == None:
            return list_1
        return list(set(list_1) - set(list_2))

    def add_reverse_association(self, object_name, trait):
        '''this builds the reverse trait to object_name association using a dictionary of a dictionary structure'''
        if trait in self.reverse_association.keys():
            self.reverse_association[trait].add_count(object_name)
        else:
            self.reverse_association[trait] = Dictogram()
            self.reverse_association[trait].add_count(object_name)

    def build_associations(self, object):
        object_name = object['name']
        object_traits = object['traits']
        traits_checked = list() # keeps track of traits we've already checked in this object
        for trait in object_traits: # for each trait in that object
            
            if self.reverse_association_bool == True: # builds the reverse trait to object associations
                self.add_reverse_association(object_name, trait)

            if trait not in self.nodes.keys(): # if we don't have that trait as a node
                    self.nodes[trait] = self.create_node(trait) # we create it

            traits_checked.append(trait) # keeps track of traits we've already checked in this object
            for other_trait in self.subtract_sets(object_traits, traits_checked): # we look at all other traits that haven't been checked yet
                association = self.calc_association(object_traits, trait, other_trait)

                self.nodes[trait].add_count(other_trait, association) # add the association value to the first node

                if other_trait not in self.nodes.keys(): # if we don't have that trait as a node
                    self.nodes[other_trait] = self.create_node(other_trait) # we create it
    
                self.nodes[other_trait].add_count(trait, association) # build the association in the opposite direction as well

    def generate_nodes(self, objects):
        ''' Runtime is O(N^2) (where N is the number of objects) because each 
            trait needs to be check against the other traits in each object'''
        for object in objects: # for each object
            self.build_associations(object)
    
    def sort_nodes(self):
        for node in self.nodes.keys():
            self.nodes[node].sort()
            

def main():
    import sys
    # arguments = sys.argv[1:]

if __name__ == '__main__':
    main()