# Data types are very basic and consist of 3 real types
# - Integer (Whole Number) {aka int()}
# - Float (Decimal Number) {aka float()}
# - String (letters) {aka str()}
# - Boolean (True/False) {aka bool()}

# Lets play around with some!
# Python syntax to defining variables are really easy.
# You just have to type the variable name and set it equal to something!

a = 5

# In this case, we have set a to have the integer value of 5
# We will be checking what we set our variables with the print() function
# We can also see our data type by using the type() function
# Check your console to see outputs

print(a) # Prints 5
print(type(a)) # Prints <class 'int'>

# Now lets set a to be 5.6

a = 5.6

# And check again

print(a) # Prints 5.6
print(type(a)) # Prints <class 'float'>

# Notice how a doesn't show 5 again.
# This is obvious, as we redefined what a was after defining it, so it essentially overwrites our previous data
# Be careful defining variables!

# Lets set a to "Hello World" and check

a = "Hello World"

print(a) # Prints "Hello World"
print(type(a)) # Prints <class 'str'>

# Booleans
# Booleans can only have 1 of 2 values: True or False
a = True # Notice how True is written, the case matters!
b = False # Same thing here!
print(a,b)
print(type(a))
print(type(b))