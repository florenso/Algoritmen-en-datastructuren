from collections import Counter
from operator import itemgetter

def readFile(fileName):
    f = open(fileName,'r') # open een file om uit te lezen
    full_text = ""
    for line in f:
        full_text += line
    return full_text


def convertTextToList(the_text):
    for i in the_text:
        if not i.isalpha():
            the_text = the_text.replace(i , ' ')
    return [x for x in the_text.split(' ') if x]

def findWordFrequencyMethod1(full_text):
    full_text = Counter(full_text)
    return sorted(full_text.items(), key=itemgetter(0))

def findWordFrequencyMethod2(full_text):
    print("Todo")




print("Method one is: ", findWordFrequencyMethod1(convertTextToList(readFile("kip.txt"))))