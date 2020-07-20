#Dictonaries are "bags" of values,each with its own label
# Dictonaries allow us to do fast-database-like operation in Python
purse = dict() #Empty constructor, building dictionary from scratch
#Order in dictionaries are random
purse['money'] = 2000
purse['candy'] = 1
print(purse) 
purse['candy'] += 5 #Contents on a dictionary are mutable
print(purse)

#To check if key exists in dictionary
print('lipstick' in purse)
#dict.get() checks if a key is already in the dictionary and assumes a default value if key is not in dictionary
#The perk of this method is that it does not traceback
print(purse)
print(purse.get('money',0)) #0 is the default value if money not found
print(purse.get('gel',0)) #0 is the default value if gel not found
print(purse)
items = ['money','candy','gel','tissues']
for item in items:
    purse[item] = purse.get(item,0)+1 #get method is an easier way to look if a key is not added, and for accumulating values
print(purse)

##################### DICTIONARIES AND FILES #################### 
wordFrequency = dict()
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except:
    print("Invalid file")
    quit()

for line in fhandle:
    words = line.split()
    for word in words:
        wordFrequency[word] = wordFrequency.get(word,0)+1 # fast handling for counting 

print(wordFrequency)
#Looping on dictionaries

for key in wordFrequency:
    print(key, wordFrequency[key])

#Retrievieng lists of keys and values
print(list(wordFrequency)) #List with all keys
print(wordFrequency.keys()) # List with all keys
print(wordFrequency.values()) #List with all values of keys
print(wordFrequency.items()) # list of tuples

#The perk of tuples are double iterations
frequentWord = None
frequencyforWord = None
for x,y in wordFrequency.items():
    if frequencyforWord is None or y> frequencyforWord:
        frequentWord = x
        frequencyforWord = y

print('More frequent word:',frequentWord,'Frequency:', frequencyforWord)
