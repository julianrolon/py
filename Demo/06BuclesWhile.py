#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""
import random

# 06) LOOPS WHILE

random_num = random.randrange(0,20)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,20)

i=0;
    
while(i<=20):
    if(i%2==0):
        print(i,"ev")
    elif(i==9):
        print(i, "break")
        break
    else:
        print(i , "else")
        i+=1
        continue
    i+=1
    