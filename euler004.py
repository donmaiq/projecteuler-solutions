def is_palindrome(arg):
    string = str(arg)
    rev = ""
    x=len(string)-1
    while x>-1:
        rev += string[x]
        x -= 1
    if string == rev:
        return True
    else:
        return False

a=999
b=999
c=91
d=99
result=[]
for x in range(0,100):
    if is_palindrome(a*b):
        result.append(str(a)+" "+str(b))
    a -= 1
    for x in range(0,100):
        if is_palindrome(a*b):
            result.append(a*b)
        b -= 1
    b=999
print(max(result))
        
        
