str = "A man, a plan , a canal--panama!?"
str = "A man, a plan , a canal--panama!?"
li= str.split(" ")
s1 = "".join(li)
print(s1)
lis= s1.split(",")
s2 ="".join(lis)
print(s2)
list=s2.split("-")
s3="".join(list)
print(s3)
list1=s3.split("!?")
s4="".join(list1)
print(s4)
x=s4.casefold()
print(x)
if (x== x[::-1]):
    print("string is a palindrome")
else:
    print("string is not a palindrome")
