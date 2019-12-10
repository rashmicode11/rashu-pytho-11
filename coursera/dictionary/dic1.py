#Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.
with open('words.txt') as f:
  words_lines = f.readlines()
words_table = []
for line in words_lines:
    parts = line.split()
    for part in parts:
      words_table.append(part)
      text = {}
      for word in words_table:
          if word not in text:
              text[word] = 1
          else:
              text[word] = + 1
              print(text)