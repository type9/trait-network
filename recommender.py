from traitnetwork import TraitNetwork
from dependencies.dictogram import Dictogram

class DrinkRecommender():

    def __init__(self, drink_list):
        # accepts a list of drinks to reccommend from and a list of preferred ingredients in descending order
        self.network = TraitNetwork(drink_list, sorted=True, reverse_association=True)
        # self.preference = ingredients

        # configurable traversing values
        self.min_association = 0.3 # minimum value to traverse a node path. if association is lower we ignore the path
        self.search_radius = 5 # how many nodes from the origin we are willing to search

    def calc_distance_modifier(self, distance):
        modifier = 1/distance
        return modifier
    
    def get_node(self, node_name):
        return self.network.nodes[node_name]

    def get_recommendations(self, origin_node):
        drink_list = [] # stores drinks found with their respective score in the format (drink, score)
        checked_ingredients = [] # stores ingredients we've already checked and scored their drinks for

        def note(this_node): # the method we call at each node we traverse
            checked_ingredients.append(this_node.name)
            print(this_node.name)

        def traverse(current_node, node_depth=0):
            '''This traverse has the base case that we have searched all associated nodes already,
            or we're already at maximum search radius'''
            branch = 0 # tracks which branch we are on for this particular node
            this_node = current_node

            note(this_node) # as we traverse each node we call a function to write down information about the node

            def get_next(this_node, checked_nodes): # defines how we find the valid next node
                nonlocal branch
                node_items = list(current_node.items())
                for i in range(branch, len(node_items), 1): # search all child nodes starting with the branch we're on
                    node_name = node_items[i][0]
                    node_weight = node_items[i][1]
                    if node_name in checked_nodes or node_weight <= self.min_association: # if we've already checked the node or the association between the two nodes is too low, we skip that node
                        branch += 1
                        continue
                    branch += 1
                    return self.get_node(node_name)
            
            next_node = get_next(this_node, checked_ingredients)
            while next_node and node_depth < self.search_radius: # while there is a valid next node, and we're within the search radius
                new_depth = node_depth + 1 # increment depth

                traverse(next_node, new_depth) # recall this method with the new depth

                next_node = get_next(this_node, checked_ingredients)

        traverse(self.get_node(origin_node))
                