# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Project Euler / Problem 1 
# Tolga Kirt / 02.2017
# -----------------------------------------------------------------------------
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# -----------------------------------------------------------------------------

# Start accumulator from zero
finalSum = 0

# Loop over all numbers in the given range
for x in xrange(0,1000):

	# Check for being multiple of 3
	if((x % 3) == 0):
		finalSum += x
	# Check for being multiple of 5		
	else:
		if((x % 5) == 0):
			finalSum += x
	
# Print out the final result
print "Result is: " + str(finalSum)
