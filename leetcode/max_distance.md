# max distance between two unequal elements

> Given an array A[], find the maximum distance between two unequal elements of the given array. Return -1 if all elements are equal.
> 
> Examples:
>> Input: A = [3, 2, 1, 2, 1]
>> 
>> Output: 4 
>> 
>> Input: A = [3, 3, 1, 3, 3] 
>> 
>> Output: 2 

## brute force solution

```
def maxDistance(A):

  d_max = -1
  
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[i] != A[j]:
        d_max = max(d_max, j-i)
  return d_max
```

Complexity: O(n^2)

## optimal solution

If the first and last elements are unequal, then they give the max distance.

In general, the max distance pair must contain either the first or last element, or both of them.

Consider the following case,
> a, a, b, b, ...., b, b, a, a, a
The max distance pair is either given by the leftmost a and the rightmost b, or the leftmost a and rightmost b.

Therefore, we can loop from A[0] until we find an index i where A[i] unequals A[-1].
Next, loop from A[-1] until we find A[-j] != A[0]. Compare the two distances.


```
def maxDistance(A):

    n = len(A)
    
    # check if first and last element are unequal
    # if yes, they give the max distance
    
    if A[0] != A[-1]:
        return n - 1
        
        
    # search from left
    
    i = 0
 
    while i < n - 1:
        if A[i] == A[n-1]:
            i += 1
        else:
            break
        
    if i == n - 1:
        d_left = -1 
    else:
        d_left = n - 1 - i
 
    # search from right
    
    i = n - 1
 
    while i > 0:
        if A[i] == A[0]:
            i -= 1
        else:
            break
 
    if i == 0:
        d_right = -1 
    else: 
        d_right = i
 
    ####

    d_max = max(d_left, d_right)
    return d_max
```

Complexity: O(n)
