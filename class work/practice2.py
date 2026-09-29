"""
i=1
n=int(input("enter number,   "))
    
while (i<=n):
    print(i)
    i=i+2



n=int(input("enter number,   "))
i=n

while (i>=1):
    print(i)
    i=i-1


i=2
n=int(input("enter number,   "))

while (i<=10):
    print(i)
    i=i+2

    
i=5
while (i<=25):
    print(i)
    i=i+5

i=1
while(i<=9):
    print(i)
    i=i+2

i=1
totalsum=0
while (i<=15):
    print(i)
    totalsum=totalsum+i
    i=i+1

print(totalsum,"total sum is")

evecount=0
evesum=0
i=2
while(i<=10):
    print(i)
    evecount=evecount+1
    evesum=evesum+i
    i=i+2

print(evecount,"is even count")
print(evesum,"is even sum")



totalsum=0
i=3
while(i<=15):
    print(i)
    totalsum=totalsum+i
    i=(i+3)

print(totalsum, "sum is ")


i=1
while(i<=3):
    
    n=int(input("ente your lcuky number :  "))
    print("ypur lucky numebr is:", n)
    i=i+1

i=1
totalsum=0
while(i<=4):
    n=int(input("enter value;  "  ))
    print(n )
    totalsum=totalsum+n

    i=i+1
print(totalsum, "is total sum")

"""

negcount=0
i=1
while(i<=5):

    n=int(input("enter value:  "))
    if n<0:
        print(n, "the value is negative")
        negcount=negcount+n

    else:
        print(n, "the numebr is positive")

    i=i+1


print(negcount, "is negative sum")

          



