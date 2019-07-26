# Functions!
# Sometimes, some tasks need to be performed multiple times within a program
# Let's look at an example.

def check_leap_year(year): 
  if year % 4 == 0:
    return "It is a leap year."
  else:
    return "It is not a leap year."

# A function may be defined using the def keyword. 
# Function definitions may include parameters, which provide data input to the function.
# Functions may also return a value using the return keyword followed by the value to return.

# In this example, a function check_leap_year is defined with parameter x.
# The function takes the year, finds the remainder when it's divided by 4, and returns a string based on the result.

# This is the general structure for a function:
# def function_name(first_parameter, second_parameter, and so forth):
#    { BODY }
#    return something

# Let's go step by step.
# For the first line, we don't have to have parameters.
# But you always need def, followed by the function name, parentheses, and a colon.

def do_my_homework():

# Python uses indentation to identify blocks of code
# Code within the same block should be indented at the same level
# All code under a function declaration should be indented to identify it as part of the function
# There can be additional indentation within a function to handle other statements such as for and if,
# so long as the lines are not indented less than the first line of the function code.

# Sometimes functions require input to provide data for their code
# This input is defined using parameters.

# Parameters are variables that are defined in the function definition
# They are assigned the values which were passed as arguments when the function was called, elsewhere in the code.

def write_a_book(character, setting, special_skill):
	print(character + " is in " + 
        setting + " practicing her " + 
        special_skill)

# For example, the function definition defines parameters for a character, a setting, and a skill
# They are all used as inputs to write the first sentence of a book

# Let's look at another example.
def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I’m ready for school!")

# Python functions can also have multiple parameters
# Just as you wouldn’t go to school without both a backpack and a pencil case, 
# functions may also need more than one input to carry out their operations.

# To define a function with multiple parameters, parameter names are placed in a comma-separated list,
# within the parentheses of the function definition.

# Let's see another example.
def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth;

# Python functions can be defined with named arguments which may have default values provided.

# Let's go back to our first example function.
def check_leap_year(year): 
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."
    
 # A return keyword is used to return a value from a Python function
 # The value returned from a function can be assigned to a variable which can then be used in the program
 # In this example, the function check_leap_year returns a string which indicates
 # if the passed parameter is a leap year or not.
 
 # Now, what if you want to return multiple values?
def square(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
 
 # Return all three values: return x_squared, y_squared, z_squared
 # All values that should be returned are listed after the return keyword and are separated by commas.
