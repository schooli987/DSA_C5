# Tuple with current order of runners
starting_order = ("Raju", "Kavya", "Issac", "Arun", "Lizy")

# Dictionary of runner weights in Kgs
weights = {
    "Arun": 52,
    "Raju": 60,
    "Kavya": 55,
    "Issac": 65,
    "Lizy": 58
}

# Step 1: Convert tuple into a list for sorting
runner_list = []
for name in starting_order:
    runner_list.append((name, weights[name]))

# Step 2: Apply Selection Sort based on weight (Descending order)
n = len(runner_list)
for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if runner_list[j][1] > runner_list[max_index][1]:  # descending
            max_index = j
    # Swap
    runner_list[i], runner_list[max_index] = runner_list[max_index], runner_list[i]

# Step 3: Display new sorted order
print("New starting line-up (by weight, descending):")
for name, weight in runner_list:
    print(name, "-", weight, "kg")
