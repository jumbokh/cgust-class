#### 針對每個元素分別處理
```
a=[1,-11,25,-39]
b=[abs(i) for i in a]
b
output:
[1, 11, 25, 39]
```
```
def add(c):    
    return c**2
l = [1,2,3]
d1 = map(add,l)
print(d1)
d2 = [c**2 for c in l]
print(d2)
d3 = [add(c) for c in l]
print(d3)
```
