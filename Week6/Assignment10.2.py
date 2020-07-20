# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
messagesHours =  dict()
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
        hour = words[5].split(':')[0]
        messagesHours[hour] = messagesHours.get(hour,0)+1

messagesHoursSorted = sorted([(key,value) for key,value in messagesHours.items()])
for key,value in messagesHoursSorted:
    print(key,value)
