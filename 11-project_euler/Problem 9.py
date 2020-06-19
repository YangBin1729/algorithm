
for c in range(334,998):
    for b in range((1000-c)//2,(1000-c)):
        a=1000-b-c
        if a**2+b**2==c**2:
            print(a,b,c)
            print(a*b*c)

