# List (Array)
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Adding elements
fruits.append("orange")
print(fruits)

# List Slicing
print(fruits[1:3])

# Removing elements
fruits.remove("banana")
print(fruits)

# Clearing the list
fruits.clear()
print(fruits)  # Output: []

# Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Adding elements to a tuple is not allowed, tuples are immutable

# Set
my_set = {1, 2, 3, 4}
print(my_set)

# Accessing elements
for item in my_set:
    print(item)

# Adding elements to a set
my_set.add(5)
print(my_set)

# Removing elements from a set
my_set.remove(2)
print(my_set)

# Clearing the set
my_set.clear()
print(my_set)  # Output: set()

# Difference between sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # Output: {1}
print(set2.difference(set1))  # Output: {4}


# Disjoint sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

# Dictionary(HashMap)
my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Accessing elements
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

# Adding elements
my_dict["city"] = "New York"
print(my_dict)

# Removing elements
del my_dict["age"]
print(my_dict)

# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}
