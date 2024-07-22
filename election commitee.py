#input 1:6
#1 2 1 1 2 2
#output:-1
#EXPLANATION : AS THE CONTESTANTS GOT SAME VOTERS THEIR IS NO MAJORITY
#INPUT 2: 10
#1 2 2 5 3 4 4 5 5 6
#OUTPUT:5
#2222
#n = int(input())
#arr = list(map(int,input().split(" ")))
n = 10
arr = [9,9,9,3,3,3,1,1,1,5]
counter = {}
for i in arr:
    if i in counter:
        counter[i] +=1
    else:
        counter[i] = 1
#print(*counter.items()) 
newArray = list(counter.items())
newArray.sort(key = lambda ele: ele[1])
#print(newArray)        
if newArray[-1]>newArray[-2]:
    print(newArray[-1])
else:
    print(-1)
#lambda function will due to its flexibility        