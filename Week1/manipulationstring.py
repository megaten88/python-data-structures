#Concatenate with '+'
a = ' Hello '
b = ' World '
c = a +' '+b
print(c)

# 'in' keyword can also be used to check to see if one string is "in" another string
print('el' in a)
print('el' in b)

#Compare strings
#Capital letter are less than miniscule letters C<a
#z>Z

#Library
print(a.lower()) # lowers case
print(a.upper()) # uppers case
dir(a) # dir() brings all capabilites of an object  
a.find('el') #finds substring and returns a position value else returns -1
b.replace('o','x') # replaces substring
a.lstrip() # removes whitespace from left
a.rstrip() #removes whitespace from right
a.strip() # removes whitespace both beginning and end

