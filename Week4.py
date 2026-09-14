# Use global variable is equal to 0 


total_sum = 0

# Use def function 
def add_to_sum(num):
        global total_sum 
        total_sum +=num

# Here use def function to display answer 
def display_sum():
        print(f"Total Sum:{total_sum}")

# Call the functions 
add_to_sum(5)
add_to_sum(10)
add_to_sum(20)
display_sum()

# Here I learn how to use global variable 
# how to take global variable for addition 
# Then how to use display function for answer 

