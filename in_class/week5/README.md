# Week 5

*September 21, 2021 — September 27, 2021*

## In-Class Exercise 6

### Part 1: Asterisks nested loop

Write a Python program `tri_asterisk.py` that uses nested `for` loops to draw this pattern (10 `*`s in the top row and 10 columns long):

```
*********
********
*******
******
*****
****
***
**
*
```

```python
for row in range(11, 1, -1):
    for column in range(row-1):
        print('*', end='')
    print()
```

![e6-part1.png](assets/e6-part1.png)

### Part 2: Hashes nested loop

Write a Python program `tri_hash.py` that uses nested `for` loops to draw this pattern (10 columns long):

```
##
# #
#  #
#   #
#    #
#     #
#      #
#       #
#        #
#         #
```

```python
for row in range(0, 10, 1):
    print('#', end='')
    for column in range(row):
        print(' ', end='')
    print('#')
```

![e6-part2.png](assets/e6-part2.png)
