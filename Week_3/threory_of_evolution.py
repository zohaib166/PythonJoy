# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:22:37 2024

This code simulates naive form of genetic algorithm in which it shows
how a gene sequence changes in hundreds of years. A list containing 
a lot of random 1s and 0s is read and with a decided probability
a randomly chosen bit is changed.

Lets consider in our case the gene changes once a year

@author: Zohaib
"""

# create a file containing random 1s and 0s
import random

gene_seq = [random.choice([0,1]) for _ in range(101)]


def evolve():
    ind = random.randint(0,len(gene_seq)-1)
    p = random.randint(1, 365)
    if p == 1:

        if gene_seq[ind] == 0:
            gene_seq[ind] = 1
        else:
            gene_seq[ind] = 0
         
print(gene_seq)

for i in range(0,10000):
    evolve()
    
print(gene_seq)


        


        

