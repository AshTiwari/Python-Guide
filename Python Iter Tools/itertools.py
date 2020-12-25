#itertools

from itertools import product

print('\nPrinting cartesian product of two list.')
cartesian_product = list(product([1,2,3],['a','b','c']))
print(cartesian_product)


print('\nPrinting cartesian product using repeat.')
cartesian_product = list(product([1,2,3],repeat = 3))
print(cartesian_product)



from itertools import permutations

print('\nPrinting permutation of 2 digits from a list.')
permutation = list(permutations([1,2,3],2))
print(permutation)


print('\nPrinting permutation of 2 alphabets from a string.')
permutation = list(permutations('abc',2))
print(permutation)


from itertools import combinations

print('\nPrinting combination of 2 digits from a list.')
combination = list(combinations([1,2,3],2))
print(combination)


from itertools import combinations_with_replacement

print('\nPrinting combination with replacement.')
combination = list(combinations_with_replacement([1,2,3],2))
print(combination)









