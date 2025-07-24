# Post Office Parcel Sorting Program

# Step 1: Take input from the user as city names
user_input = input("Enter parcel destination cities (separated by spaces): ")

# Step 2: Convert the input string into a list of city names
cities = user_input.split()

# Step 3: Print cities before sorting
print("\nBefore sorting:")
print(cities)

# Step 4: Apply Selection Sort to sort the cities alphabetically
n = len(cities)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if cities[j] < cities[min_index]:
            min_index = j
    # Swap the current city with the minimum city found
    cities[i], cities[min_index] = cities[min_index], cities[i]

# Step 5: Print the sorted list
print("\nAfter sorting (Alphabetical by City Name):")
print(cities)
