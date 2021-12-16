#!/usr/bin/env python
# coding: utf-8

## problem: given a positive integer n, return true if n is a power of 2.

## solution 1: if n is odd, return false; if n is even, keep deviding n by 2 until either n = 1 (return true) or n is odd (return false)
## time complexity: O(log n)

def isPower(n):
    if n == 1:
        return True
    
    else:
        while n > 1:
            if n%2 != 0:
                return False
            if n%2 == 0:
                n = n/2
            if n == 1:
                return True

## solution 2: same algorithm, but written in a recursive way.

def isPower(n):
    
    if n == 1:
        return True
    
    if n%2 != 0:
        return False
    
    return isPower(n/2)


## solution 3: start from an initial guess num = 1, keep multiplying num by 2 until num >= n.

def isPower(n):
        num = 1
        
        while num <= n:
            if num == n:
                return True
            num = num * 2
            
        return False


## solution 4: bitwise operation
## in binary form, n can be written by 0...010...0 and n-1 by 0...001...1, if n is a power of 2. 
## then we apply & operation on n and n-1, leading to 0...000...0. 

## time complexity: O(1)


def isPower(n):
    return (n & n-1) == 0


