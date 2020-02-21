# python class and init


class self:
    def __init__(self):
        print('\nFirst class.')
        print('Self argument is passed automatically.')
        print('Printing self: '+ str(self))
        
class multiple_init:
    def __init__(self):pass
    def __init__(self):
        print('\nSecond Class.')
        print('In case of multiple __init__ only the last init is considered.')
        print('All previous __init__ area overridden.')

class  rename_self:
    def __init__(not_self):
        print('\nThird Class.')
        print('"self" is just a general convention. We can rename it to anything.')


self()
multiple_init()
rename_self()
