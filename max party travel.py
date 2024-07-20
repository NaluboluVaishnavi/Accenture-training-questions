#4hrs= 4*60 = 240 min
#time to travel = 100 min
#total time = 60min
#1 2 3 4 5 6.....100
#5 10 15 20 25 30....500
#1st problem =5min => 60 - 5 = 55 min
#2nd problem =10min => 55 - 10 = 45min
#3rdproblem = 15min => 45 - 15 =30 min                           #5 #180
#4th problem = 20min => 35 -20=10 min
#5th problem = 25min => you cannot solve this prob

n=int(input())#no of problems
travel_time = int(input()) #travelling time
time_remaining = 240 - travel_time #calculating remaining time
count = 0
for i in range(1, n+1):
    solve_time = i*5
    if solve_time < time_remaining and time_remaining > 0:
     count += 1 # counting the solved problems 
     time_remaining -= solve_time
     
print(count) #answer    