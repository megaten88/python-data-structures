#using open(filename,mode) ==> pass filename and 'r'(for reading) or 'w' (for writing)
# open() returns a file handle
fhandle = open('test.txt','r') #fhandle.read() will bring all the file in a single line
count = 0
for sequence in fhandle: #for automatically handles the file content as sequences
    count+=1
