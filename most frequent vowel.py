s = input()
d ={ 
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
for i in s:
    if i in "aeiou":
        d[i] += 1
#print(*d.items())
ans,maxvalue = '',0
#for ele in list(d.items()):
    #print(ele[0],ele[1]
for key, value in list(d.items()):
    if value > maxvalue:
        ans = key
        maxvalue = value
print(ans)               