# regular expression.

import re                       

message = ('Call at +91-9280690895 or +91-9920699095')
RegExpObj = re.compile(r'\+\d\d-\d\d\d\d\d\d\d\d\d\d')      #raw string as an input argument.


#findall()
print('\n\nfindall()')
print('Prints all regular expression and its group.')
m_o = RegExpObj.findall(message)                #makes 'm_o' a list,prints all the regexp found in message.
print('Printing the variable type returned and its value by findall() ')
print(type(m_o))
print(m_o)


#search()
print('\n\nsearch()')
m_o = RegExpObj.search(message)     #match_object searches the expresion in the message
print('Printing results of searcch()')
print(m_o)
print(type(m_o))

#group()                            #next step of search()
print('\n\ngroup()')
m_o = RegExpObj.search(message)
if m_o ==None:
    print('Phone Number not found.')
else:
    print('Looking for a phone number in a message using group().')
    print(m_o.group())                 #mo.group() shows the first regExp found.

#We can break a reg-exp into multiple groups.

RegExpObj2 = re.compile(r'(\+\d\d)-(\d\d\d\d\d\d\d\d\d\d)')     #Area code and phone no.
match_object2 = RegExpObj2.search(message)

if match_object2 ==None:
    print('Phone Number not found.')
else:
    print('Printing 1st group i.e area code.')
    print(match_object2.group(1))               #prints the 1st group of exp found.
    print('Printing 2nd group i.e. phone no.') 
    print(match_object2.group(2))               #prints the 2nd group of expression found.

    
#pipe character:'|' and curly braces: '{}'
print('\n\nPipe Charcter and {}')
print('Here, we can use "+" or "0" interchangebly because of pipe "|".')
RegExpObj3 = re.compile(r'((\+|0)\d{2})-(\d{10})')     #| => or ;{n} => repeated n times.
message = ('Call me at +91-9999900000 or 022-2222200000')
m_o3 = RegExpObj3.search(message)

if m_o3 ==None:
    print('Phone Number not found.')
else:
    print('Printing all groups')
    print(RegExpObj3.findall(message))
    print('Printing each group')
    print(m_o3.group(1))
    print(m_o3.group(2))
    print(m_o3.group(3))
    #print(m_o3.group(4))
    #print(m_o3.group(5))       # how to print next three group of second regex found. 
    #print(m_o3.group(6))
    

#Repetition of expressions.
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




# greedy and non-greedy search
print('\n\n\nGreedy and non-greedy search.\n')

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

