# verbose

import re

msg = 'Email me at ashu.atiwa@gmail.com or ashtiwari1498@yahoo.com'
print("Verbose just makes the progrm look good. It dosen't change the output.")

emailRegex = re.compile(r"""( 
            [a-z0-9_.-]+              # local Part 
            @                             # single @ sign 
            [0-9a-z]+                # Domain name 
            \.                            # single Dot . 
            [a-z]{2,6})                 # Top level Domain   
             """,re.VERBOSE | re.IGNORECASE)

print(emailRegex.findall(msg))

