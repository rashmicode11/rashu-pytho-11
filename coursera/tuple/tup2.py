d = {'a': 10, 'b': 1, 'c': 22}
l = list()
for key, val in d.items():
 l.append((val, key))
 print(l)
 l= [(10, 'a'), (22, 'c'), (1, 'b')]
 l.sort(reverse=True)
 print(l)