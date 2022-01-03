# converting a list to a string

## list of strings

Suppose I have a list, 
```
myList = ['particle', 'physics', 'is', 'fun']
```
how can I convert it to a string 
```
myString = 'particle physics is fun'
```

* method 1: use `join()`:
```
' '.join(myList)
```
Note that `''.join(myList)` will return `'particlephysicsisfun'` without white space.

* method 2: adding list elements to an empty string

Initialize an empty string: `myString = ' '`. Then traverse the list, and add every element to `myString`:
```
for s in myList:
    myString += ' ' + s
```



## list of integers

Suppose now I have a list `myList = [1, 2, 3]` and I want to return `myString = '123'`. 

```
''.join(str(num) for num in myList)
```

