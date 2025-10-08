
list1 = [1, 2, 3]
list2 = [4, 5, [6, 7]]


nested = [list1, list2]
print("Nested List:", nested)


print("Length of list1:", len(list1))


print("Concatenation:", list1 + list2)


print("Is 3 in list1?", 3 in list1)

print("Elements in list1:")
for i in list1:
    print(i)

print("First element:", list1[0])
print("Slicing [1:]:", list1[1:])
