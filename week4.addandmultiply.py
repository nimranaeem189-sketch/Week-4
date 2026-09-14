#functions where one function calls another to take the result and do further processing
# Example 1: Basic Arithmetic Operations

# Use def function 

# First we add two numbers 
def add(a,b):
    return a+b

# Use def function we multiple two numbers 
def multiply(x,y):
    return x*y

# Using function of def and multiply for answer 
def add_and_multiply(a,b,c):
    sum_result =add(a,b)   #Calling the add function
    product_result=multiply(sum_result,c)   #Calling the multiply function
    return product_result

# From this I learn how to use basic Arithmetic operationfor result

result=add_and_multiply(2,3,4)
print(result)     #Output:20