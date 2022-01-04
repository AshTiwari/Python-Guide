# select P plates from N stacks of K plates.

def knapsack(n, k, p, values):
    valuesSum = [[0 for i in range(p+1)] for i in range(n+1)]
    for stack in range(n+1):
        for plate in range(k+1):
            if stack == 0 or plate == 0:
                valuesSum[stack][plate] = 0
            elif plate == 1:
                valuesSum[stack][plate] = values[stack-1][plate-1]
            else:
                valuesSum[stack][plate] = values[stack-1][plate-1] + valuesSum[stack][plate - 1]

    knapsack = [[0 for i in range(p+1)] for i in range(n+1)]

    for stack in range(n+1):
        for plate in range(p+1):
            if stack == 0 or plate == 0:
                knapsack[stack][plate] = 0
            else:
                for i in range(plate+1):
                    temp = valuesSum[stack][i] + knapsack[stack-1][plate- i]
                    knapsack[stack][plate] = max(knapsack[stack][plate], temp)
                    
    return knapsack[n][p]

if __name__ == "__main__":
    #values = [[10, 10, 100, 30],[80, 50, 10, 50]]
    values = [[80, 80], [15, 50], [20, 10]]
    n, k, p = 3, 2, 3
    print(knapsack(n, k, p, values))
