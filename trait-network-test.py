from trait-network import TraitNetwork

class GenericObj():
    def __init__(self, name):
        self.name = name
        self.traits = {}
    
    def add_trait(self, name, value):
        self.traits[name] = value

def main():
    import sys
    arguments = sys.argv[1:]

if __name__ == '__main__':
    main()