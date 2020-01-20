# verbose
import re

print('Verbose allows us to add space or newline character even when the are not present in our regular expression.')

msg1 = ' Call me at +91-9999900000 or 022-9999900000'
print('Message: '+msg1)

phoneRegex = re.compile(r'''
(+|0)\d\d   #area code with 022 or +91
-
\d{10}      # 10 digit phone number.''',re.VERBOSE)

print(phoneRegex.findall(msg1))



#####################
''' CHECK ERROR '''
###################
