N=int(input())
count = 0
for a in range(1,int(N**0.5)+1):
    for b in range(1,int(N**0.5)+1):
        for c in range(1,int(N**0.5)+1):
            if(a*a)+(b*b)+(c*c)+(a*b)+(b*c)+(c*a) == N:
                count += 1
print(count)                

