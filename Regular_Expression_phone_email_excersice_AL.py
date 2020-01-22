#! python3
# phoneAndEmail.py -Al-Sweigart version.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)



# TODO: Create email regex.
emailRegex = re.compile(r'''(
   [a-zA-Z0-9._!#$&%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   \.[a-zA-Z]{2,4}       # dot-something
    )''', re.VERBOSE)

# TODO: Get the text off the clipboard.
text = pyperclip.paste()

# TODO: Extract the email/phone from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#TODO: Copy the extracted email/phone to the clipboard.

results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail)

pyperclip.copy(results)




