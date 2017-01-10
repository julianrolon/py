#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""

# 03) TUPLES LIKE A BALLOON... Can't be modified

pi_tuple = (3,1,4,1,5,9)

new_list = list(pi_tuple)
new_tuple = tuple(new_list)

#print(pi_tuple.count)
print(len(pi_tuple))
print(min(pi_tuple))