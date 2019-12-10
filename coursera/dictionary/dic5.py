lineslist=[]
emaildict={}
with open("mbox-short.txt") as f:
  for line in f:
    lineslist = line.split()
    if line.startswith('From '):
      email=lineslist[1]
      if email not in emaildict:
        emaildict[email] = 1
      else:
        emaildict[email] += 1
print (emaildict)