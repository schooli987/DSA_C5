# Tuple with current order of runners
starting_order = ("Ravi", "Zara", "Imran", "Anaya", "Liam")

# Dictionary of runner heights
heights = {
    "Anaya": 150,
    "Ravi": 165,
    "Zara": 145,
    "Imran": 170,
    "Liam": 160
}

# Step 1: Convert tuple into a list for sorting
runner_list = []
for name in starting_order:
    runner_list.append((name, heights[name]))

# Step 2: Apply Selection Sort based on height
n = len(runner_list)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if runner_list[j][1] < runner_list[min_index][1]:
            min_index = j
    # Swap
    runner_list[i], runner_list[min_index] = runner_list[min_index], runner_list[i]

# Step 3: Display new sorted order
print("New starting line-up (by height):")
for name, height in runner_list:
    print(name, "-", height, "cm")
