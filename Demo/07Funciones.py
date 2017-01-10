#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""
import sys

# 07) FUNCTIONS

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum
    
string = addNumber(1,4)

print(string)
    
print("What is your name?")
name = sys.stdin.readline()
print("Hola ",name)
