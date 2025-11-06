# 0/1 Knapsack Problem

# Taking user input
n = int(input("Enter number of items: "))
W = int(input("Enter capacity of knapsack: "))

value = []
weight = []

for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

# Create DP table
dp = [[0]*(W+1) for _ in range(n+1)]

# Fill table
for i in range(1, n+1):
    for j in range(1, W+1):
        if weight[i-1] <= j:
            dp[i][j] = max(value[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# Output result
print("Maximum Profit Earned:", dp[n][W])
