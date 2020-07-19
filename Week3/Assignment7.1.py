#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name
try:
    fname = input("Enter file name: ")
except:
    print("Invalid file")
    quit()
fhandle = open(fname,'r')
for line in fhandle:
    print(line.rstrip().upper())