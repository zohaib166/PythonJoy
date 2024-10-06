# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:10:59 2024

@author: hasan
"""

def check_prime(num):
    if num==2 or num==3:
        return True
    i = 2
    
    flag = True
    
    while(i*i <= num):
        if(num%i != 0):
            i+=1
        else:
            flag = False
            break
        
    return flag

num = int(input())
sum = 0

for i in range(2,num+1):
    if check_prime(i) == True:
        sum += i
    
print(sum,end="")
            
        