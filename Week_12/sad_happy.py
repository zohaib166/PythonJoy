# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:41:30 2024

@author: hasan
"""


def sad_happy(num,iterations):
    happy = num
    sad = 0
    
    for _ in range(iterations):
        new_happy = happy * 0.3 + sad * 0.5
        new_sad = happy * 0.7 + sad * 0.5
        happy,sad = new_happy,new_sad
        
    return int(happy), int(sad)


def find_sad_happy(num):
    recur(num,0)
    
count = 3   
def recur(happy,sad):
    global count
    if count>0:
        count-=1
        recur(happy*0.3 + sad*0.5, happy*0.7+sad*0.5)
    else:
        print(int(happy), int(sad),end="")
    
num = int(input())
find_sad_happy(num)
#print(happy, sad, end="")
    
        