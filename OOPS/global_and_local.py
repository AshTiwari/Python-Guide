#Global and Local Scope/Variable

print('#Global and local scope/variable. \n')

'''
-A local scope is a scope within a function.
-A global scope is a scope outside the function, and covers rest of the area.
-Global and local scope are mutually exclusive and exhaustive
i.e
- they never share a same region

- addition of both the scope  gives the whole program.

Local scope and variable:
-variable defined in a local scope is a loal variable.
-this scopes starts when a function is called and ends when the function
returns the value.

Global scope and variable:
-variable defined in global scope is gobal variable.
-global scope starts when the program starts and terminates when the program
terminates.

#a global and local variable can have same name.
#to turn a local vaariable to global variable we use keyword global.

print('Code in global scope cannot access local variable.')
print('Code in local scope can acess global variable.')
print('Code of first functions local scope cannot access variable of second function local scope.')
'''



print('Printing global variable before creating any local scope.')
variable=20
print('Global variable = '+str(variable))

def first_funct():
    print('printing local variable with same name as global variable')
    variable='twenty'
    print('Local variable = '+variable)
    
def second_funct():
    print('printing global and local variable with different name.')
    local_variable='twenty'
    print('Local variable = '+local_variable)
    print('Global variable = '+str(variable))

def third_function():
    print('printing variable with same name as local var but has keyword global.')
    global variable
    variable='twenty'
    print('local variable = ' +str(variable))
    print('check above error later.')

first_funct()
second_funct()
third_function()

