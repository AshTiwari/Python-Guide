# greedy and non-greedy search

print('Greedy and non-greedy search.\n')

print('Python by defult uses greedy search method')
print('i.e it will find the longest possible search.')
reo = re.compile(r'(\d){3,5}')
mo = reo.search('1234567890')
print(mo.group())

print('To use non greedy search method use "?"')
print('i.e it will find the shortest possible search.')
reo = re.compile(r'(\d){3,5}?')
mo = reo.search('1234567890')
print(mo.group())

