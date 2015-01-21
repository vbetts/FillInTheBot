__author__ = 'victoriabetts'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import random
import configparser
import json

config = ConfigParser.ConfigParser()
config.read('.twitter')

consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')
stream_rule = config.get('app', 'rule')
account_screen_name = config.get('app', 'account_screen_name').lower() 
account_user_id = config.get('app', 'account_user_id')


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
def Create_List(filename, list):
    with open(filename) as openfile:
        for word in openfile:
            #Python appends a newline character when reading from a text file. We have to strip that character.
            wordFix = word.replace('\n', '')
            list.append(wordFix)
        return list

Create_List(nFILENAME, nouns)
Create_List(vFILENAME, verbs)
Create_List(acFILENAME, actions)
Create_List(adFILENAME, adjectives)
Create_List(anFILENAME, animals)
Create_List(cFILENAME, colours)
Create_List(sFILENAME, sports)

print ("[v] = verb      [n] = noun      [ac] = action    [ad] = adjective")
print ("[an] = animal       [c] = colour        [s] = sport")
print ("")

userSentence = input("Enter a sentence! Use the above key to create 'blanks': ")

def fill_in_the_blanks(sentence):
    
    while True:
        #For each loop, select a new random number for each blank
        nounNum = random.randint(0, len(nouns))
        verbNum = random.randint(0, len(verbs))
        actionNum = random.randint(0, len(actions))
        adjNum = random.randint(0, len(adjectives))
        anNum = random.randint(0, len(animals))
        colNum = random.randint(0, len(colours))
        spNum = random.randint(0, len(sports))
        
        #Find each incidence of the word key and replace it with a randomly generated word from each list
        text = sentence.replace('[n]' and '[N]', nouns[nounNum], 1)\
            .replace('[ad]' and '[AD]' and '[Ad]' and '[aD]', adjectives[adjNum], 1)\
            .replace('[v]' and '[V]', verbs[verbNum], 1)\
            .replace('[ac]' and '[AC]' and '[Ac]' and '[aC]', actions[actionNum], 1)\
            .replace('[an]' and '[AN]' and '[An]' and '[aN]', animals[anNum], 1)\
            .replace('[c]' and '[C]', colours[colNum], 1)\
            .replace('[s]' and '[S]', sports[spNum], 1)
        if text == sentence:
            break
        sentence = text
    return text

print(fill_in_the_blanks(userSentence))

