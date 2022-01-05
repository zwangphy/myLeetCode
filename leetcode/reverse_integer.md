

```
class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        elif x > 0:
            y = int(str(x)[::-1])
            if y > pow(2,31)-1: 
                return 0
            else:
                return y
       
        elif x < 0:
            return -self.reverse(-x)
```         
