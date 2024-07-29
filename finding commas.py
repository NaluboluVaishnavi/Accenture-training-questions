#n=1000
#1 2 3 4 5 6..... 999 1,000.
#ans=1
#n=2000
#1-999 -> 0 commas
#1000-2,000 -> 1000 commas
#counting number of commas
#3 digit numbers=>1-999 = 0
#4 digits number=>1,000-9,999=>1 comma each
#5 digits number=>10,000-99,999=>1 comma each
#6 digits number=>100,000-999,999=>2 comma each
# n=1000
# 1,2,3,4
# 1->(1-1)//3->0
# 2->0 
#3->(2)//3=>0
#4->(3)//3=>1
#5000
n=int(input())
digits = len(str(n))
total = 0
for i in range(1,digits):
    commas_per_number = (i-1)//3
    how_many_nums = 9 *(10**(i-1))
    total += commas_per_number*how_many_nums
    #print(f"for {i} length digits,total commas are {commas_per_number*how_many_nums}")
commas_per_number = (digits-1)//3
how_many_nums*(n - (10**(digits-1)))+1
total += commas_per_number*how_many_nums
print(total)        
