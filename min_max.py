#Author: Jasmine Singh
#Github Username: Jassig98
#Date: October 11, 2022
#Description: Project 3A

print("How many integers would you like to enter?")
N=int(input())
count=0
print("Please enter",N,"integers.")
while(count<N):
    N_1=int(input())
    if(count==0):
        min=N_1
        max=N_1
    else:
        if(max<N_1):
            max=N_1
        if(min>N_1):
            min=N_1
    count+=1
print("min:",min)
print("max:",max)

