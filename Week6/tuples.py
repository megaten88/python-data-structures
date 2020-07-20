#Tuples are another kind of data structure similar to lists, they have elements indexed starting at 0
#Tuples are between parenteses
x = ('X','Y','Z')
print(x[1])
print(max(x))

# However, tuples are "immutable", cannot alter its content
#Tuples cannot be sorted,appended, reversed etc..
# We can also put tuples on the left-hand side of an assignment statement
(a,b) = (1,2)
print(a)
print(b)

#Tuples are comparable
print((0,1,2) < (5,1,2)) #It compares the leftmost number.... 0<5 in this example
print((0,1,3) < (0,5,2)) # If the leftmost are equal on both tuples, it compares the next item on each 1<5    

#On a dictionary, to sort items() use the function sorted(), it sorts in key order
d = {'a':10,'c':15,'b':20,'m':45,'z':26}
print(sorted(d.items()))
#We can sort by reverse by adding the parameter
print(sorted(d.items(),reverse=True))

# We can order by values as well
sortByValue = sorted([(value,key) for key,value in d.items()]) # using dynamic list
print(sortByValue)
#We can reverse it as well to get the highest values first
sortByValue = sorted([(value,key) for key,value in d.items()],reverse=True) 
print(sortByValue)