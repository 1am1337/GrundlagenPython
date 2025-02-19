mySet = {1,2,3}
newSet = {4,5,6}
testSet = {1,2,3,4,5,6,7,8,9}
mySet.add(1)
print(mySet)
mySet.update(newSet)
print(mySet)
mySet.remove(6)
print(mySet)
mySet.discard(6)
print(mySet)
removed = mySet.pop()
print(removed, mySet)
mySet = {1,2,3,4}
newSet = {3,4,5,6}
print(mySet.union((newSet)))
print(mySet.intersection(newSet))
print(mySet.difference(newSet))
print(mySet.symmetric_difference(newSet))
print(mySet <= testSet)
print(1 in mySet)