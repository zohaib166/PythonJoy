# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:11:24 2024
Joy of Computing using python: Week 3: Fizzbuzz
Description: Given a series of numbers, print Fizz if the number is divisible by 3, 
print Buzz if the number is divisible by 5 and print FizzBuzz if the number is divisible
by both 3 and 5 otherwise, just print the number
@author: Zohaib
"""

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"= FizzBuzz")
    else:
        if i % 3 == 0:
            print(i,"= Fizz")
        elif i % 5 == 0:
            print(i,"= Buzz")
        else:
            print(i,"=")
