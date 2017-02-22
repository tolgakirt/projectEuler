# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Project Euler / Problem 3 
# Tolga Kirt / 02.2017
# -----------------------------------------------------------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# -----------------------------------------------------------------------------

#our number is n

n = 600851475143

#smallest prime factor
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)