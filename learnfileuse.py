myfile = open('textfile', 'r')
line = myfile.readline()
myfile.close()

with open('duplicate', 'w') as dupe:
    dupe.write(line)
    print("file successfully copied")
