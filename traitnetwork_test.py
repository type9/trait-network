from traitnetwork import TraitNetwork
from collections import namedtuple
from recommender import DrinkRecommender

class GenericObj():
    def __init__(self, name):
        self.name = name
        self.traits = {}
    
    def add_trait(self, name, value):
        self.traits[name] = value

drink1 = {'name': 'After Dinner Cocktail',
        'traits': {'Apricot Brandy': 0.33, 'Lime': 0.33, 'Triple sec': 0.33}}

drink2 = {'name': 'Amaretto Mist',
        'traits' : {'Amaretto': 0.6, 'Lime': 0.4}}

drink3 = {'name': 'ArchBishop',
        'traits': {'Gin': 0.4, 'Lime': 0.2, 'Green Ginger Wine': 0.2, 'Benedictine': 0.2}}


Drink = namedtuple('Drink', ['name', 'ingredients'])  # like defining a Drink class

drink_list = [drink1, drink2, drink3]

def main():
    import sys
    arguments = sys.argv[1:]
    drink_network = DrinkRecommender(drink_list)
    drink_network.get_recommendations('Lime')


if __name__ == '__main__':
    main()