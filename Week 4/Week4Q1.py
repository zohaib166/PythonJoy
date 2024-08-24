# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:43:48 2024

Magic square - a n by n grid of numbers where the addition of all the rows/cols/diag
will end up as the same number M

M = n(n^2+1)/2

Steps to construct a magic square:
    1. 1 is always located at (n/2,n-1)
    2. Let this position of 1 by (p,q). 2 will be placed at (p-1,q+1).
        IF the row position becomes -1, then make it n-1 or if the column position 
        becomes n make it 0
    3. if the calculated position already contains a number then decrement the column by 2
    and increment the row by 1
    4. if the any time the the row position becomes -1 AND columns becomes n, switch it to (0,n-2)

@author: hasan
"""

