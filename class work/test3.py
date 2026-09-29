




    #s=to find how many are odd and even 
    #to find how the total oddsum and even susm
i=1
evecount=0
oddcount=0
evesum=0
oddsum=0
totalsum=0


while(i<=4):
    n=int(input("enter number : "))
    if(n%2==0):
      print(n ,"the number is even")
      evecount=evecount+1
      evesum=evesum+n


    else:
       print(n ,"the number is odd")
       oddcount=oddcount+1
       oddsum=oddsum+n

    totalsum=totalsum+n



    i=i+1 
      
print("even count is", evecount)
print("odd count is",  oddcount)
print("even sum is ",  evesum)
print("odd sum is ",  oddcount)
print("total sum is",   totalsum)










