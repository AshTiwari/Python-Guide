#pipe character:'|' and curly braces: '{}'

import re                       
    
print('Pipe Charcter and {}')
print('Here, we can use "+" or "0" interchangebly because of pipe "|".')
RegExpObj = re.compile(r'((\+|0)\d{2})-(\d{10})')     #| => or ;{n} => repeated n times.
message = ('Call me at +91-9999900000 or 022-2222200000')
m_o = RegExpObj.search(message)

if m_o ==None:
    print('Phone Number not found.')
else:
    print('Printing all groups')
    print(RegExpObj.findall(message))
    print('Printing each group')
    print(m_o.group(1))
    print(m_o.group(2))
    print(m_o.group(3))
    #print(m_o.group(4))
    #print(m_o.group(5))       # how to print next three group of second regex found. 
    #print(m_o.group(6))
    

