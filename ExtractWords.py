__author__ = 'victoriabetts'

"""
I had a series of text files with lists of words, but the nouns and verbs came in various tenses and agreements.
I decided that the best way to proceed was to extract the simplest, singular form of each word and write those words
to new text files. I identified each verb ending in 's', 'ed' or 'ing', and each noun ending in 's' and excluded them 
from my new list. This is imperfect, due to the idiosyncrasies of language, but it works for my purposes.
"""

MAX_VERBS = 4874
MAX_NOUNS = 5449

verbList = []
nounList = []

verbFileName = 'verb.txt'
nounFileName = 'noun.txt'

newVerbFileName = 'verblist.txt'
newNounFileName = 'nounlist.txt'

verbFile = open(verbFileName)
newVerbFile = open(newVerbFileName, 'w')

nounFile = open(nounFileName)
newNounFile = open(newNounFileName, 'w')

iVerbs = 0
iNouns = 0

while (iVerbs <= MAX_VERBS-1):
    verb = verbFile.readline()
    wordFix = verb.replace('\n', '')
    if not wordFix.endswith('s') and not wordFix.endswith('ed') and not wordFix.endswith('ing'):
        verbList.append(wordFix)
    iVerbs+=1

print (verbList)

for word in verbList:
    newVerbFile.writelines(word + '\n')

while (iNouns <= MAX_NOUNS-1):
    noun = nounFile.readline()
    wordFix = noun.replace('\n', '')
    if not wordFix.endswith('s'):
        nounList.append(wordFix)
    iNouns+=1

print (nounList)

for word in nounList:
    newNounFile.writelines(word + '\n')