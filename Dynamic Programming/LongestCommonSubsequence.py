# Longest Common Subsequence.

def lcsRecursion(str1, str2):
    n = len(str1)
    m = len(str2)

    if n == 0 or m == 0:
        return 0
    elif str1[-1] == str2[-1]:
        return 1 + lcsRecursion(str1[:-1], str2[:-1])
    else:
        return max(lcsRecursion(str1[:-1],str2), lcsRecursion(str1, str2[:-1]))


def lcsDp(str1, str2):
    n = len(str1)
    m = len(str2)

    LCS = [[None for i in range(m+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,m+1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            
    return LCS[-1][-1]

str1 = "adbsc"
str2 = "abgc"
print(lcsRecursion(str1, str2))
print(lcsDp(str1, str2))
