#search(pattern) and group()


import re                       

message = ('Call at +91-9280690895 or +91-9920699095')
RegExpObj = re.compile(r'\+\d\d-\d\d\d\d\d\d\d\d\d\d')      #raw string as an input argument.

#search()
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
