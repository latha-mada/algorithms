#!/usr/bin/python

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

n=3
print "factorial of 3=%d " %factorial(3)
