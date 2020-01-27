#DEBUGGING - raise exception

'''
create box.
####
#  #
####
'''
'''
raise Exception cretes Traceback.
Traceback help us find the origin of the problem.
'''

def buildBox(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('The length of "symbol" should be 1.')
    if width < 2 or height < 2:
        raise Exception('The width and height should be equal or more than 2.')

    print(symbol*width)

    for i in range(height - 2):
        print(symbol +' '*(width-2)+symbol)

    print(symbol*width)

buildBox('*',10,5)
    
