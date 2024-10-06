# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:18:13 2024

@author: hasan
"""

count = 0;
def collatz(num):
    global count
    count+=1
    if(num%2==0 and num>1):
        return collatz(num/2)
    if(num%2!=0 and num>1):
        return collatz(num*3+1)
    return count-1

print(collatz(27))