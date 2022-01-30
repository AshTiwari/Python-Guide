# floyd warshall

def floydWarshall(weight, n):
    dp = [[None for i in range(n)]for j in range(n)]
    nextIndex = [[None for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = weight[i][j]
            nextIndex[i][j] = j if weight[i][j] != float("inf") else None

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    nextIndex[i][j] = k
    
    negCycleVertex = []             
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    negCycleVertex.append(j)
    
    for j in negCycleVertex:
        for i in range(n):
            dp[i][j] = float("-inf")
    
    if len(negCycleVertex) == 0:
        return dp, nextIndex
    else:
        return dp, []

if __name__ == "__main__":
    inf = float("inf")
    weight = [[0,3,inf,inf,inf,2],[inf,0,1,inf,inf,inf],[inf,inf,-1,2,inf,inf],[inf,inf,inf,0,2,inf],[inf,inf,inf,inf,inf,inf],[inf,inf,inf,inf,1,0]]
    n = 6
    dp, nextIndex = floydWarshall(weight, n)

    print("The distance matrix:")
    print(dp)
    print("NextIndex Matrix:")
    print(nextIndex)

    
