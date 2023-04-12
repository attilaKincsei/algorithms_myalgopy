"""
Source: https://www.codewars.com/kata/total-increasing-or-decreasing-numbers-up-to-a-power-of-10/train/python
build a function to return the total occurrences of
all the increasing or decreasing numbers
below 10 raised to the xth power (x will always be >= 0).
"""


def total_inc_dec(x):
    largest_number = 10 ** x
    
