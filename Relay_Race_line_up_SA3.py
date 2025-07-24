# Mission 3 – Relay Race Line-Up (String Sorting)

# Step 1: Take input as a string of names
user_input = input("Enter runner names separated by spaces: ")

# Step 2: Convert the string to a list of names (no conversion to int)
names = user_input.split()

# Step 3: Print names before sorting
print("Before sorting:")
print(names)

# Step 4: Apply Selection Sort to sort alphabetically
n = len(names)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if names[j] < names[min_index]:
            min_index = j
    names[i], names[min_index] = names[min_index], names[i]

# Step 5: Print sorted names
print("After sorting (Alphabetical Order):")
print(names)
