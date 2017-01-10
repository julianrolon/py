#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:02:23 2017

@author: julianrolon
"""

# 02) LIST
grocery_list = ["Juice","Tomatoes","Potatoes","Bananas"]
grocery_list[0]="Onions"
#print (grocery_list[0])
#print (grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events,grocery_list]
print(to_do_list[0][1])
grocery_list.append("Lettuce")
grocery_list.append("Bananas")
grocery_list.insert(1,"Pickle")
grocery_list.remove("Bananas")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[0]
grocery_list = other_events + grocery_list 
print(grocery_list)
print(len(grocery_list))
print(max(grocery_list))
print(min(grocery_list))

