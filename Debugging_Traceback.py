#Traceback error log

import traceback

try:
    raise Exception('This line has caused an error.')
except:
    errorFile = open('D://erroLog.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info has been written in the log.')
    
