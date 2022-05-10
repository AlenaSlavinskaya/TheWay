import random

a = [random.randint(1,100) for i in range(10)]
# a[3] = 1
a = tuple(a)
print(a)
print(a.index(min(a)),a.index(max(a)))
