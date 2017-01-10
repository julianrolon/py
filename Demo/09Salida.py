#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""
import os
# 09) IO

test_file = open("test.txt","wb") # ab+ read and append (opens or create)

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file\n",'UTF-8'))
test_file.close()

test_file = open("test.txt","r+")
text_in_file = test_file.read()
print(text_in_file)

os.remove("test.txt")


