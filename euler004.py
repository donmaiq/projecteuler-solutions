import time
start=time.time()

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
result=[]
for x in range(0,100):
    for x in range(0,100):
        if is_palindrome(a*b):
            result.append(a*b)
        b-=1
    a-=1
    b=999
print(max(result))

end=time.time()
print(str(round(end-start,3))+" seconds")
        
