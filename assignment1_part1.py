#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is part 1 of the Assignment 1


#The below function returns the number of integer
def listDivide(numbers, divide=2):
  
    divisible = []
    for number in numbers:
        if (int(number) % int(divide)) == 0:
            divisible.append(number)
    listlen = len(divisible)
    return listlen

#This is the exception class
class ListDivideException(Exception):
    
    pass

#This function will test the listDivide function
def testListDivide():

    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Caught Exception!")
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Caught Exception!")
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Caught Exception!")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Caught Exception!")
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Caught Exception!")


testListDivide()
