# handling exception. try and except.

def div42by(x):
    try:
        print(42/x)
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except NameError:
        print('Cannot divide by char/string or unassigned variables')
        print('Check why the output of above line is errorneous.')
    except:
        print('Any other error.')  #useful for input validation



div42by(2)
div42by(0)
div42by('*')
div42by(a)
