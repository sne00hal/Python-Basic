b = set()
print(type(b))

b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))


print(b)


print(len(b)) # Prints the length of this set


b.remove(5) # Removes 5 fromt set b


print(b)

print(b.pop())
print(b)