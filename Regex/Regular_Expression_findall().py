#findall()

import re                       

message = ('Call at +91-9280690895 or +91-9920699095')
RegExpObj = re.compile(r'\+\d\d-\d\d\d\d\d\d\d\d\d\d')      #raw string as an input argument.

print('Prints all regular expression and its group.')
m_o = RegExpObj.findall(message)                #makes 'm_o' a list,prints all the regexp found in message.
print('Printing the variable type returned and its value by findall() ')
print(type(m_o))
print(m_o)
