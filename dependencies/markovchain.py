from dictogram import Dictogram

class Node(Dictogram):
    def __init__(self, word):
        super(Node, self).__init__()
        self.word = word # the word that this node represents
        self.status = str()
    
    def walk(self): 
        '''chooses a node to walk to based off of sample'''
        return self.sample()

class MarkovChain():
    def __init__(self, text):
        self.nodes = self.generate_nodes(text)
        self.heads = Dictogram(text)
    
    def generate_nodes(self, text):
        '''iterates across list of words creating a list of nodes'''
        nodes = {} # seperate list to keep track of nodes we've already added and their respective object

        for word in range(len(text)): # for each word in the text we're analysing
            this_word = text[word]

            if this_word in nodes.keys(): # if the word has already been added as a key
                if not (word + 2) > len(text): # checks that next word index is inbounds
                    nodes[this_word].add_count(text[word + 1]) # add a token of the next word
            else:
                nodes[this_word] = Node(this_word) # if not we create a new node
                if not (word + 2) > len(text): # checks that next word index is inbounds
                    nodes[this_word].add_count(text[word + 1]) # add a token of the next word

        return nodes
    
    def generate_sentence(self, num_words):
        '''generates a sentence with max-length (n) of words'''
        sentence = str()

        this_word = self.heads.sample() # samples text histogram in order to find a lead node
    
        for i in range(num_words):
            sentence += this_word # word gets appended onto the sentence

            if self.nodes[this_word].types == 0: # checks if we're at a end node
                return sentence

            if not i == num_words: # if we're not on the last word
                sentence += ' ' # adds a space

            this_word = self.nodes[this_word].walk() # samples the current node for the next word

        return sentence
        

def main():
    import sys
    arguments = sys.argv[1:]

    my_chain = MarkovChain(arguments)
    print(my_chain.nodes)
    print(my_chain.generate_sentence(5))

if __name__ == '__main__':
    main()