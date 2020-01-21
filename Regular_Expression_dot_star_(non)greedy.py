# dot star greedy and non greedy

import re

msg ='Message : <To serve humans> for dinner.>\n'
print(msg)

#by default greedy:
greedyRegex = re.compile(r'<.*>')
print('Printing default greedy search between <>')
print(greedyRegex.findall(msg))


#non greedy:
nonGreedyRegex = re.compile(r'<.*?>')
print('\nPrinting non greedy search using ?')
print(nonGreedyRegex.findall(msg)[0])
