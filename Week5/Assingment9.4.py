#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
senders =  dict()
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except:
    print("Invalid file")
    quit()

for line in fhandle:
    if 'From ' in line:
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender,0) + 1

frequentSender = None
emailFrecuency = None
for x,y in senders.items():
    if frequentSender is None or y> emailFrecuency:
        frequentSender = x
        emailFrecuency = y

print(frequentSender,emailFrecuency)