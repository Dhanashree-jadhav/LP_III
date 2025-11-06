# Fractional Knapsack Problem using Greedy Method

# Take number of items from user
n = int(input("Enter number of items: "))

# Create list to store [profit, weight]
arr = []

# Take profit and weight for each item
for i in range(n):
    p, w = map(float, input(f"Enter profit and weight of item {i+1}: ").split())
    arr.append([p, w])

# Take knapsack capacity
capacity = float(input("Enter capacity of knapsack: "))

# Sort items based on profit/weight ratio (descending)
arr.sort(key=lambda x: x[0]/x[1], reverse=True)

max_profit = 0.0

for profit, weight in arr:
    if capacity == 0:
        break
    if weight <= capacity:
        # Take full item
        max_profit += profit
        capacity -= weight
    else:
        # Take fractional part
        max_profit += profit * (capacity / weight)
        capacity = 0

print("Maximum Profit =", max_profit)
