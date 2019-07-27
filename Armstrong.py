#Armstrong number algo

arm=input("Enter the number")

n=len(arm)

j=0

for i in arm:
    j=int(i)**n+j
    
if (str(j)==arm):
    print("{} is Armstrong numer".format(arm))
else:
    print("{} is not Armstrong number".format(arm))
