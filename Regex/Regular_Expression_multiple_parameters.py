#multiple parameters in re.compile

import re

msg = 'Hello ,\nI am robocop number 1.\nGet Lost!!!'

regex = re.compile(R'''
        ^HELLO      # should start with hello
        .*          # can contain any character
                    ''',re.I | re.DOTALL | re.VERBOSE)


print(regex.findall(msg))
