first = "apple"
second = "banana"

# print them out
print(f"First: {first} | second {second}")

# now switch them
first, second = second, first

print("I've switched things around...")
print(f"First: {first} | second {second}")