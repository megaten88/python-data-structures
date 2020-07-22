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

string  = 'This is a this message with this in it'
print(string.count('this')) #Counts how many times a substring appear, method is case sensitive

print(string.endswith('it')) #Returns either True or False if the string ends with the determined substring
print('123'.isnumeric()) #Returns either true or false if string can be converted to int
join_message = "/".join(["This","is","a","joined","string"]) # A method that joins a list of strings with the delimeter stated before the .join, in this case '/'
print(join_message)

#we can also format strings, passing variables to strings.
#.format() deals with any type of data
name="Mayra"
age=23
print("My name is {}. I'm {} years old".format(name,age))
# There is many ways to do this
print("My name is {name}. I'm {age} years old".format(name="Maeia",age=age*3))

# another example
def student_grade(name, grade):
	return "{person} received {percent}% on the exam".format(person=name,percent=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Format is also really useful for currency display, especially with formating expressions
price = 7.5
tax_rate = 1.09
print("Base price: ${:.2f}; With Taxes: ${:.2f}".format(price, tax_rate*price))

# Another format example
def to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

for degree in range(0,101,10):
    print("{:>10}F | {:>11.2f} C".format(degree, to_celsius(degree))) # > operator aligns to the right >number determines the number of spaces to be aligned

print(name[::-1])