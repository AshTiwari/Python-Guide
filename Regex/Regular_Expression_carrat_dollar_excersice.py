#difference between(start dot star end) and carrat-start dot star end-dollar.

import re

msg1 = 'Hello I am a robocop'
msg2 = 'Hello I am a robocop.'


print('Is (Hello .* robocop) and (^Hello .* robocop$) same?')
print('Ans: no ^ and $ will search the text in the message and having ^ and & makes sure that Hello and robocop are at extremes.')

nonExtremeRegex = re.compile('Hello .* robocop')
print('\nWithout ^ and $ on msg1 and msg2.')
print(nonExtremeRegex.findall(msg1))
print(nonExtremeRegex.findall(msg2))

ExtremeRegex = re.compile('^Hello .* robocop$')
print('\nWith^ and $ on msg1 and msg2.')
print(ExtremeRegex.findall(msg1))
print(ExtremeRegex.findall(msg2))
print("Because of . after robocop, $ dosen't match the pattern. ")



