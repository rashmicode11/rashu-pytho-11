lineslist=[]
domaindict={}
with open("mbox-short.txt") as f:
  for line in f:
    lineslist = line.split()
    if line.startswith('From '):
      email=lineslist[1]
      domain = email.split('@')[1] #.split creates list, and [1] returns 2nd item in list
      if domain not in domaindict:
        domaindict[domain] = 1
      else:
        domaindict[domain] += 1
print (domaindict)