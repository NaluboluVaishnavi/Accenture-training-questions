#6
#331112
#[11]
n=int(input())
arr=list(map(int,input().split(" ")))
count = {}
for num in arr:
    if num in count.keys():
        count[num] += 1
    else:
        count[num] = 1
newArr = []
for num,freq in count.items():
    [freq]*num)       