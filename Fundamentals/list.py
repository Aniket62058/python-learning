l = []

l.append(5)  # l = [5]
l.append(4)  # l = [5,4]
l[1] = 10  # list is mutable
#   l = [5,10]
print(l)

l.remove(5)  # remove if you know the value
del l[0]  # remove if you know index
print(l)
