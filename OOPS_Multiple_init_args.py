# multiple __init__

class multiple_argument:
    def __init__(self, *args):
        print('\n1st class: Multiple arguments.')
        print('We can give *args argument to __init__.')
        print('It means tuple of arguments.')
        print('So now, while calling the class we can choose to not gie any argument at all or give any number of arguments')

class multiple_key_arg:
    def __init__(self, **kwargs):
        print('\n2nd Class: Dictionary arguments i.e. key-value type argument.')
        print('We can use **kwargs')

class hybrid:
    def __init__(self, *args, **kwargs):
        print('\n3rd Class: We can give both the tule and dict of arguments.')
        print('We use *args, **kwargs.')
        print('Objects will have to pass the arguments in same order.')
        print('Here, single args will we passed first and then keyed arguments.')

name =   'ashu'
roll_no = 1
multiple_argument(name,roll_no);
multiple_key_arg(name = 'ashu');
hybrid( roll_no,name = 'ashu' );
