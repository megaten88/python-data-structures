#Collection: is a set of values
friends = ['Faby','Brian','Chicha','Raquel','Chicha']
#Lists are surrounded by brackets and the elements in it are separated by commas.
#Lists can be any Python object, even another list
#We can get elements from lists by using an index specified in square brackets
print(friends[0])
#Lists are mutable, we can change an element of a list using index operator, unlike strings, which cannot be mutated
friends[2] = 'Ana'
print(friends)
# len() takes lists as parameters and returns the number of elements in it
print("Number of friends:", len(friends))
#range() returns a list of numbers  that range from zero to one less than the parameter
#we can construct an index loop using for and integer iterator
length = len(friends)
print(range(length))

for i in range(len(friends)):
    friend = friends[i]
    print("Friend",friend, "is at:", i)

#Slicing 
print(friends[2:3])
print(friends[:3])

#Building from scratch
random = list() #constructor
random.append(1)
random.append(2)
random.insert(0,3) # insert() inserts an element at the defined position in the first argument
print(random)

#check item on list
print(2 in random)
#Built-in functions
print(len(random)) #prints number of elements
print(max(random)) # prints maximum number
print(min(random)) # prints minimum number
print(sum(random)) # prints sum of all numbers

#str.split() returns a list'
string = "Transform this to a list"
stringList = string.split() #split also accepts a delimiter split(',') etc..
print(stringList)
