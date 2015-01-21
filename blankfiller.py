import random

class BlankFiller:
    nouns = []
    verbs = []
    actions = []
    adjectives = []
    animals = []
    colours = []
    sports = []
    
    nFILENAME = "nounlist.txt"
    vFILENAME = "verblist.txt"
    acFILENAME = "actionlist.txt"
    adFILENAME = "adjectivelist.txt"
    anFILENAME = "animallist.txt"
    cFILENAME = "colorlist.txt"
    sFILENAME = "sportlist.txt"
    
    #Read from the text files and add each word to our defined lists
    def Create_List(self, filename, list):
        with open(filename) as openfile:
            for word in openfile:
                #Python appends a newline character when reading from a text file. We have to strip that character.
                wordFix = word.replace('\n', '')
                list.append(wordFix)
            return list
    def __init__(self):
        self.Create_List(self.nFILENAME, self.nouns)
        self.Create_List(self.vFILENAME, self.verbs)
        self.Create_List(self.acFILENAME, self.actions)
        self.Create_List(self.adFILENAME, self.adjectives)
        self.Create_List(self.anFILENAME, self.animals)
        self.Create_List(self.cFILENAME, self.colours)
        self.Create_List(self.sFILENAME, self.sports)
    
    #print ("[v] = verb      [n] = noun      [ac] = action    [ad] = adjective")
    #print ("[an] = animal       [c] = colour        [s] = sport")
    #print ("")
    
    #userSentence = input("Enter a sentence! Use the above key to create 'blanks': ")
    
    def fill_in_the_blanks(self, sentence):
        
        while True:
            #For each loop, select a new random number for each blank
            nounNum = random.randint(0, len(self.nouns)-1)
            verbNum = random.randint(0, len(self.verbs)-1)
            actionNum = random.randint(0, len(self.actions)-1)
            adjNum = random.randint(0, len(self.adjectives)-1)
            anNum = random.randint(0, len(self.animals)-1)
            colNum = random.randint(0, len(self.colours)-1)
            spNum = random.randint(0, len(self.sports)-1)
            
            #Find each incidence of the word key and replace it with a randomly generated word from each list
            text = sentence.replace('[n]', '[' + self.nouns[nounNum] + ']', 1)\
                .replace('[ad]', '[' + self.adjectives[adjNum] + ']', 1)\
                .replace('[v]', '[' + self.verbs[verbNum] + ']', 1)\
                .replace('[ac]', '[' + self.actions[actionNum] + ']', 1)\
                .replace('[an]', '[' + self.animals[anNum] + ']', 1)\
                .replace('[c]', '[' + self.colours[colNum] + ']', 1)\
                .replace('[s]', '[' + self.sports[spNum] + ']', 1)
            if text == sentence:
                break
            sentence = text
        return text
    
    #print(fill_in_the_blanks(userSentence))
    
