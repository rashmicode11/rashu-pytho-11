fname = input("Enter file name: ")
fh = open(fname)
numlist = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    numlist.append(words)
    for word in numlist:
        if word != numlist:
            del word
            print(numlist)
