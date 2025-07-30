course = "Python Beginners"
length = len(course)
print(length)

print(len(course))


print(course[0])  # First character
print(course[6])  # Seventh character
print(course[-2])  # Second to last character

print(course[0:5])  # First five characters
print(course[5:])  # From the sixth character to the end
print(course[:9])  # From the start to the ninth character
# Every second character from the first to the ninth character
print(course[0:9:2])
print(course[::2])  # Every second character from the start to the end
print(course[::-1])  # Reverse the string
print(course[:])
