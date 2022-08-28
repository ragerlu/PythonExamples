#The purpose of the python-functions.py file is to provide
# examples of functions in the python programming language. 
#The lines of code below can be typed into an environment running python
#to produce the desired result which is displayed in a comment line below in [].

# A function is used to break our code into simpler parts which become easy to maintain 
#and understand.

#General template for a function:
#def function_name(parameter1:type, parameter2:type, .....):
#   statement

#Function examples:
#Sum function:
a = 2
b = 2
def sum_function(a:int, b:int):
    print(a + b)
sum_function(a, b)
#[4]

#Truth function:
c = True
d = False
e = True
def truth_function(a:bool, b:bool):
    if (a == True) and (b == True):
        print(True)
    else:
        print(False)
truth_function(c, d)
#[False]
truth_function(c, e)
#[True]