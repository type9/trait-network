from dependencies.dictogram import Dictogram
from dependencies.markovchain import MarkovChain

class Trait(Dictogram):
    def __init__(self, name):
        super(Trait, self).__init__()
        self.name = name
    
    def walk(self, index=0):
        '''should return the next connected node with the highest association by default, if index is defined then return from the index'''
        pass

class TraitNetwork():
    '''This class accepts a list of object dictionaries in the following format:
        {'obj_name':
            'trait1': 0.5,
            'trait2': 0.25,
            'trait3': 0.25} 
        trait values should represent the weighting of how much it composes of each object adding up to 1.0'''
    def __init__(self, objects):
        # generation variables
        self.nodes = {}
        self.objects = objects

        # configurable traversing values
        self.min_association = 0.3 # minimum value to traverse a node path. if association is lower we ignore the path

        # initialization

    def create_node(self, name):
        return Trait(name)

    def calc_association(self, object, trait_1, trait_2):
        '''This method will return an association value based off of a predetermined formula'''
        association = float()
        association = object[trait_1] + object[trait_2]
        return association

    def subtract_sets(self, list_1, list_2):
        if list_2 == None:
            return list_1
        return list(set(list_1) - set(list_2))
    
    def build_associations(self, object):
            object_traits = object.keys() #
            traits_checked = list() # keeps track of traits we've already checked in this object
            for trait in object_traits: # for each trait in that object
                
                if trait not in self.nodes.keys(): # if we don't have that trait as a node
                        self.nodes[trait] = self.create_node(trait) # we create it

                traits_checked.append(trait) # keeps track of traits we've already checked in this object
                for other_trait in object_traits.subtract_sets(object_traits, traits_checked): # we look at all other traits that haven't been checked yet
                    self.nodes[trait][other_trait] += self.calc_association(object, trait, other_trait) # add the association value to the node
    
    def generate_nodes(self, objects):
        ''' Runtime is O(N^2.5) (where N is the number of objects) because each 
            trait needs to be check against the other traits in each object'''
        for object in objects: # for each object
            self.build_associations(object)

def main():
    import sys
    arguments = sys.argv[1:]

if __name__ == '__main__':
    main()