s='A man,a plan,a canal--panama!?'
def palindrome(s):
    m = ""
    for j in range(len(s)):
        if s[j].isalpha():
            m = m + s[j].lower()
            #print(m)

    x = len(m) - 1
    for i in range(int(len(m)/2)):
        if m[x - i] != m[i]:
            return False
    return True
z = palindrome(s)
if z:
    print("True")
else:
    print("false")