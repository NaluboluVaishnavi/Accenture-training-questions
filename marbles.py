#N=10,A=3,B=5
#1)10-3=7
#2)7-3=4
#3)4-3=1
#4)10-5=5
#5)5-3=2
#10,7,4,1,5,2 ARE THE UNQUIE NUMBERS
#HENCE THE OUTPUT IS 6
#10 3 5
#6
N,A,B= list(map(int,input().split()))
res=set()
for i in range(N//A+1):
    for j in range(N//B+1):
        value = N-(i*A) - (j*B)
        if value>0:
            res.add(value)
print(len(res))      
print(res)      
