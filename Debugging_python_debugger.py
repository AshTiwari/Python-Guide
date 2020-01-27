#Using the debugger!!!

'''
NOTE: Run normally means without debugger.
Debugger has following buttons:
Go: Runs all code normally fast and only stops at **breakpoint**.
Step (in):Enters into function.
(Step) Over:Skips function by running normally and jumps to next line.
(step) Out:While inside a function, it will run all steps normally and
            jump out of the function.
Quit:Quit the bedugger and run normally.

How to set a breakpoint?
Ans:  Select a line, right click and select 'Set Breakpoint.'
'''

import random

#code to toss a coin 1000 times.

heads = 0

for i in range(1,1001):
        if random.randint(0,1)==1:
            heads +=1

        if i ==500:
            print('Halfway done. Breakpoint reached.')
# ^^^^ Above line is a breakpoint line. ^^^^

print('Total no. of heads is %s' %heads)
# ^^^^ Above line is a breakpoint line. ^^^^



