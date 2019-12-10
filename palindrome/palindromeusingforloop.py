s = "A man, a plan , a canal--panama!?"
list1=[" ",","--"!?"]
s5=s
for x in list1:
    s=s5
    list2=str.split(x)
    s5="".join(list2)
    print(s5)
    x=s5.casefold()
if (x== x[::-1]):
    print("string is a palindrome")
else:
    print("string is not a palindrome")
