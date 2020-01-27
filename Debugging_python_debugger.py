#Using the debugger!!!

'''
NOTE: Run normally means without debugger.
Debugger has following buttons:

1. Go: Continue program until next **breakpoint** or end of the file appears.

2. Step (in): Step into a function call.

3. (Step) Over: Step over current line of code and pause on next line.

4. (step) Out:While inside a function, it will jump out of the function.

5. Quit:Quit the bedugger and run normally.

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



