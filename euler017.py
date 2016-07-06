import time
start=time.time()

def onenumber(num):
    if num==1: return "one"
    elif num==2: return "two"
    elif num==3: return "three"
    elif num==4: return "four"
    elif num==5: return "five"
    elif num==6: return "six"
    elif num==7: return "seven"
    elif num==8: return "eight"
    elif num==9: return "nine"
    elif num==10: return "ten"
    else: return "error:num"

def teens(num):
    if num==1: return "eleven"
    elif num==0: return "ten"
    elif num==2: return "twelve"
    elif num==3: return "thirteen"
    elif num==4: return "fourteen"
    elif num==5: return "fifteen"
    elif num==6: return "sixteen"
    elif num==7: return "seventeen"
    elif num==8: return "eighteen"
    elif num==9: return "nineteen"
    else: return "error:teens"+str(num)

def tens(num):
    if num==2: return "twenty"
    elif num==3: return "thirty"
    elif num==4: return "forty"
    elif num==5: return "fifty"
    elif num==6: return "sixty"
    elif num==7: return "seventy"
    elif num==8: return "eighty"
    elif num==9: return "ninety"
    else: return "error:tens"
        

def stringify(number):
    output=""
    index=0
    if len(str(number))>3:
        output += onenumber(int(str(number)[index]))+"thousand"
        index+=1
    if len(str(number))>2:
        if str(number)[index]!="0":
            output += onenumber(int(str(number)[index]))+"hundred"
        index+=1
    if len(str(number))>1:
        if str(number)[index]!="0":
            if output!="": output+="and"
            if str(number)[index]=="1":
                output += teens(int(str(number)[index+1]))
                return output
            else:
                output += tens(int(str(number)[index]))
        index+=1
    if len(str(number))>0:
        if str(number)[index-1]=="0" and str(number)[index]!="0": output += "and"
        if str(number)[index]!="0":
            output += onenumber(int(str(number)[index]))
    return output

charcount=0
for words in range(1,1001):
    print(stringify(words))
    charcount += len(stringify(words))
print(charcount)


end=time.time()
print(str(round(end-start,3))+" seconds")
