#excersice on os module

import os

totalsize = 0

for filename in os.listdir('C:\GitHub Projects\Python-Guide'):
    if not os.path.isfile(os.path.join('C:\GitHub Projects\Python-Guide',filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('C:\GitHub Projects\Python-Guide',filename))


print(totalsize)
    



    
    
