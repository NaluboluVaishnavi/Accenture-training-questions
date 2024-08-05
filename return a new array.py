n=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
res=[]
left,right=0,0
for i in range(0,n):
    left += arr[i]
    right=total-left
    value=abs(left-right)
    res.append(value)
print(res)    