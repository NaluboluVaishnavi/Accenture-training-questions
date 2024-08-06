#4
#12343
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
left,right=0,0
score=0
for i in range(n//2):
    left,right=arr[i],arr[n-1-i]
    score += abs(left-right)
print(score)    