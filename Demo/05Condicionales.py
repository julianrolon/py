#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""

# 05) CONDITIONALS: if else elif == != > >= <=

age = 30
if age >= 21:
    print('Tractor Driver!')
elif age >= 16:
    print('You are old enough')
else:
    print('You are NOT')


# and or not

if ((age>=1) and (age<=18)):
    print ("Birthday")
elif ((age==21) or (age>=65)):
    print ("Birthday2")
elif not(age==30):
    print ("DON'T")
else:
    print ("Yeah")    