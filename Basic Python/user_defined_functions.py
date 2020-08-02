#User Defined Functions in python

# Functions

#Syntax
'''
def funct_name (parameters):
    statements
                  
    return (expression)
                  
x = funct_name(parameter_value)
#x takes the value returned by function.
#If the function dosen't return any value the x will take value 'None'. 
'''
def increment(val):
    val=val+1
    print(val)
    return val
            
x= increment(4)
print('The value returned by "increment function" is\n:')
print(x)
    
 

'''
Note:
1."def" stands for definition.
2.Parameters dosen't have types.
    => It has both advantage and disadvantage.
        1. Coding becomes easy.
        2. Debugging becomes difficult.


****************************************************** Excercise *******************************************************

1. >>  def increment(val)
    >>       val=val+1
    >>       print(val)
            
   
            

    >> x= increment(4)
    >> print(x)
    
    Predict O/P:
    
    
    Ans:4
        None
        
        The function returns 'None'. So x takes 'None'. 
        Thus, not secifying types may give results which we didn't expect at begining.
'''

