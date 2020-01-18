#more on group()

import re                       

#We can break a reg-exp into multiple groups.

RegExpObj = re.compile(r'(\+\d\d)-(\d\d\d\d\d\d\d\d\d\d)')     #Area code and phone no.
message = ('Call at +91-9280690895 or +91-9920699095')
match_object = RegExpObj.search(message)

if match_object ==None:
    print('Phone Number not found.')
else:
    print('Printing 1st group i.e area code.')
    print(match_object.group(1))               #prints the 1st group of exp found.
    print('Printing 2nd group i.e. phone no.') 
    print(match_object.group(2))               #prints the 2nd group of expression found.

    
