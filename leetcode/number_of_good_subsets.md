# Number of good subsets
https://leetcode.com/discuss/interview-question/268604/Google-interview-Number-of-subsets
> For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

## Solution 1:

Sort the list:

a[1], a[2], ..., a[i], a[i+1], ..., a[j],...

For every pair of i and j >= i, check if a[i] + a[j] <= K. If yes, then {a[i], a[j]} + any subset (including empty subset) formed by numbers between i and j is a good subset. There are j-i-1 numbers between i and j (for j >= i + 1), so the number of subset formed by these numbers is 2^(j-i-1).


```
def goodSubset(a, K):
    nums = 0    
    a.sort()    
    for i in range(len(a)):    
        for j in range(i,len(a)):
            if a[i] + a[j] <= K:
                if j <= i + 1:
                    nums += 1
                if j >= i + 2:
                    nums += 2**(j-i-1)
    return nums
 ```

Overall complexity: O(n^2)

## Better solution

Sort the list. For i, use binary search to find the max j such that a[i] + a[j] <= K.

```
```

Overall complexity: O(n logn)
