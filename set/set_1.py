a = {1,2,3,4,5,6}

b = set(['hello','world','Python'])

my_set = frozenset(['hello','world','Python'])
print(type(my_set))

a = frozenset(['hello','world','sunny'])
print(type(a))

# # print(b)

a.add('red')
print(a)
# # a.remove('red')
# a.discard(4)
# #print(a.clear())

# a = {'hello','world','sunny'}
# b = {1,8,7,6,3,2,2,2,2,2,2}
# c = {1,8,5,2,4,13,16}
# print(b.isdisjoint(a))
# print(c - b)
# print(c.union(a,b))
# print(len(a))