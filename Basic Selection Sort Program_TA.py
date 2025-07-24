# Basic Selection Sort Program

# Step 1: Create a list of numbers
numbers = [45, 30, 55, 25, 35]

# Step 2: Print the list before sorting
print("Before sorting:")
print(numbers)

# Step 3: Apply Selection Sort
n = len(numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    # Swap the smallest element with the current position
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Step 4: Print the list after sorting
print("After sorting:")
print(numbers)
