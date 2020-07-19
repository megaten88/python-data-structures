# Strings on Python start at index 0
check_string = input("Enter input: ")
# len() gives us the length of a string
check_length = len(check_string)
print("Length", check_length)
#Looping and Counting
count = 0
for letter in check_string:
    if letter == 'i':
        count+=1

print("Count:", count)

#Slicing string[0:X] the first number states where to start, X is the end of slice "up to but not included"
#If the second number is beyond the end of string, it stops at the end
print(check_string[0:5])
#If we leave off the first number or last number of the slice, it is assumed to be the beginning or the end of the string respectively.
print(check_string[6:])
print(check_string[:8])
print(check_string[:])