# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Project Euler / Problem 1 
# Tolga Kirt / 02.2017
# -----------------------------------------------------------------------------
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
# -----------------------------------------------------------------------------

def Palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

i = 100
j = 100
greatest = 0
while (i <= 999):
    while (j <= 999):
        product = i * j
        if (product > greatest and Palindrome(str(product))):
            greatest = product
            correct_i = i
            correct_j = j 
            	
        j += 1
    j = 100
    i += 1
print "Answer: " + str(greatest)

print str(correct_i) + " " + str(correct_j)