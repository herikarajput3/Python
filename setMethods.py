set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

# Union: it is used to return the union of two sets and it does not change the original sets
# print(set1.union(set2))

# Update: it is used to update the set with the elements of another set and it change the original set

# Difference between union and update is that union returns the union of two sets and update updates the set with the elements of another set

# set1.update(set2)
# print(set1)

# Add: it is used to add an element to the set and it change the original set
# set1.add(6)
# print(set1)

# isDisjoint: it is used to return True if the sets have no elements in common and it does not change the original sets

# a = {1,2,3,4,5}
# b = {6,7,8,9}
# print(a.isdisjoint(b))

# Clear: it is used to remove all the elements from the set and it change the original set
# set1.clear()
# print(set1)

# Difference: it is used to return the difference between two sets and it does not change the original sets
# print(set1.difference(set2))

# Difference Update: it is used to update the set with the difference between two sets and it change the original set

# set1.difference_update(set2)
# print(set1)

# Symmetric Difference: it is used to return the symmetric difference between two sets and it does not change the original sets
# It is opposite of intersection
# print(set1.symmetric_difference(set2))

# Symmetric Difference Update: it is used to update the set with the symmetric difference between two sets and it change the original set
# set1.symmetric_difference_update(set2)
# print(set1)

# isSubset: it is used to return True if the set is a subset of another set and it does not change the original sets
# isSuperSet: it is used to return True if the set is a superset of another set and it does not change the original sets

# a = {1,2,3,4,5,6,7,8,9}
# b = {1,2,3,4,5}
# print(b.issubset(a))
# print(a.issuperset(b))

# Copy: it is used to return a copy of the set and returns a new set
# set3 = set1.copy()
# set1.add(6)
# print(set1)
# print(set3)

# Discard: it is used to remove an element from the set and it change the original set
# set1.discard(5)
# print(set1)

# Remove: it is used to remove an element from the set and it change the original set
# set1.remove(6)
# print(set1)

# The difference between discard and remove is that discard does not raise an error if the element is not present in the set and remove raises an error if the element is not present in the set

# Intersection: it is used to return the intersection of two sets and it does not change the original sets
# print(set1.intersection(set2))

# Intersection Update: it is used to update the set with the intersection of two sets and it change the original set
# set1.intersection_update(set2)
# print(set1)

# Pop: it is used to remove and it change the original set
# set1.pop()
# print(set1)