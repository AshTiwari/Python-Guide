# python program to extract phone and email from a pdf.

import re
import pyperclip

#TODO: Create a regex object for phone numbers.
phoneRegex = re.compile(r"""
#+91-9999900000 or +919999900000 or 09999900000 or 9999900000 or
#+910000-000-000 or 09999-999-999 or 0000-000-000 or
#000-99990000 or 99990000   

#area code optional (+91 (-)?| 0)?        
#10 digit phone number  \d{4}(-)?\d{3}(-)?\d{3}
#std area code (\d{2,8}(-))?
#8 digit number \d{8}
                                   # mobile number
(((\+91(-)?|0)?
\d{4}(-)?\d{3}(-)?\d{3}
)
|                                    #or telephone number
((\d{2,8}(-))?
\d{8}
)) """,re.VERBOSE)


#TODO:Create a regex object for email address.

emailRegex = re.compile(r'''
#first par: 
# @
#domain name

(
[a-zA-Z0-9.!#$%]+
@
[a-zA-Z]+
\.
[a-zA-Z]+ )''',re.VERBOSE)


#TODO: Get the text of the clipboard.
text = pyperclip.paste()

#TODO: Extract the email/phone off this text.

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedEmail)

allPhoneNumber = []
for phoneNumber in extractedPhone:
    allPhoneNumber.append(phoneNumber[0])

print(allPhoneNumber)
#TODO: Copy the extracted email/phone to the clipboard.

