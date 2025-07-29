# Dictionary of runner names and their heights
runners = {
    "Anaya": 150,
    "Ravi": 165,
    "Zara": 145,
    "Imran": 170,
    "Liam": 160
}

# Step 1: Convert dictionary to a list of tuples (name, height)
runner_list = []
for name in runners:
    runner_list.append((name, runners[name]))

# Step 2: Apply Selection Sort based on height (index 1 of tuple)
n = len(runner_list)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if runner_list[j][1] < runner_list[min_index][1]:
            min_index = j
    # Swap tuples
    runner_list[i], runner_list[min_index] = runner_list[min_index], runner_list[i]

# Step 3: Display sorted runner names with heights
print("Runners sorted by height (shortest to tallest):")
for name, height in runner_list:
    print(name, "-", height, "cm")
