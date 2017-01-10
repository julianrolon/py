#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""

# 06) LOOPS FOR

for x in range (0,10):
    print(x,' ',end="")
    
print("\n")

grocery_list = ["Juice","Tomatoes","Potatoes","Bananas"]

for x in grocery_list:
    print (x)

for x in [2,4,6,8,10]:
    print (x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

    