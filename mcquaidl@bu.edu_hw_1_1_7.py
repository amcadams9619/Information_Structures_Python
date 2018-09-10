# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:48:56 2018

Problem 1.7
Results of both the 1st and 2nd approximations of pi are outlined below
Not necessary to import the "math" module, given these are basic calculations
"""

#First approximation of pi
result1 = 4 * (1 - (1/3) + (1/5) - (1/7) + (1/9) - (1/11))

print('The first approximation of pi is ', result1)

#Second approximation of pi
result2 = 4 * (1 - (1/3) + (1/5) - (1/7) + (1/9) - (1/11) + (1/13) - (1/15))

print('The second approximation of pi is ', result2)