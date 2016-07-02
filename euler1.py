def is_divisible(arg):
    boolean = True
    for x in range(2,21):
        if arg%x != 0:
            boolean = False
            break
    return boolean

searching = True
inc=0
printer=0
while searching:
    inc += 380
    if is_divisible(inc):
        searching=False
    if printer > 100000:
        printer=0
        print("100000 loops")
    printer +=1
print(inc)
    
