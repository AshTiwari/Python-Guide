# longest increasing subsequence.
# make a[i] >= a[j] to make it longest non decreasing subsequence.

def lisDynamic(a):
    n = len(a)
    lis = [1 for i in range(n)]
    
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j]:
                lis[i] = max(lis[i], 1 + lis[j])

    return max(lis)


a = [1,3,4,5,6,2,2,2,2,2]
print(lisDynamic(a))
            
