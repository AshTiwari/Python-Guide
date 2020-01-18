#Repetition of expressions.

import re

print('Useful characters to check the repetition of expression.')
print('{n}: check if preceding string is repeated n times.')
print('?: check if preceding string is used 0 or 1 times.')
print('*: check if preceding string is used 0 or more time.')
print('+: check if preceding string is used 1 or more times.')
print('{n}: check if preceding string is used exactly n times.')
print('{x,y}: used more than x times and less than equal to y times.')
    
# ?                                                 
print('\n\n[?,*,+,{}] character')
msg1 = 'I am sorry'
msg2 = 'I am verysorry'
msg3 = 'I am veryveryverysorry.'

pattern1 = r'(very)?sorry'
pattern2 = r'(very)*sorry'
pattern3 = r'(very)+sorry'
pattern4 = r'(very){1,2}sorry'

print('\nWorking of ? character on 3 different messages.')
reo = re.compile(pattern1)
m_o = reo.search(msg1)
print(m_o.group())
m_o = reo.search(msg2)
print(m_o.group())
m_o = reo.search(msg3)
print(m_o.group())              # matches only the last 'very' and skips the first 2.

print('\nWorking of * character on 3 different messages.')
reo = re.compile(pattern2)
m_o = reo.search(msg1)
print(m_o.group())
m_o = reo.search(msg2)
print(m_o.group())
m_o = reo.search(msg3)
print(m_o.group())

print('\nWorking of + character on 3 different messages.')
reo = re.compile(pattern3)
m_o = reo.search(msg1)
if m_o==None:
    print('No expression found in message one.')
m_o = reo.search(msg2)
print(m_o.group())
m_o = reo.search(msg3)
print(m_o.group())

print('\n{} already demonstrated with pipe character.')


print('\nWorking of {x,y} on 3 different messages.')
reo = re.compile(pattern4)
m_o = reo.search(msg1)
if m_o==None:
    print('No expression found in message one.')
m_o = reo.search(msg2)
print(m_o.group())
m_o = reo.search(msg3)
print(m_o.group())                      #matches only 2 of 'very'.



