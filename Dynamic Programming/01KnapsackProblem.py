# 0 1 knapsack problem.

def knapsack(weights, values, targetWeight):
    n = len(values)
    knapsack = [[0 for i in range(targetWeight + 1)] for i in range(n + 1)]
    for item in range(n+1):
        for cost in range(targetWeight + 1):
            if item == 0 or cost == 0:
                knapsack[item][cost] = 0
            elif weights[item-1] <= cost:
                knapsack[item][cost] = max(knapsack[item-1][cost], values[item - 1] + knapsack[item - 1][cost - weights[item-1]])
            else:
                knapsack[item][cost] = knapsack[item-1][cost]
    for row in knapsack:
        print(row)
    return knapsack[n][targetWeight]

if __name__ == "__main__":
    values = [60,50,70,30]
    weights = [5,3,4,2]
    targetWeight = 5
    print(knapsack(weights, values, targetWeight))
