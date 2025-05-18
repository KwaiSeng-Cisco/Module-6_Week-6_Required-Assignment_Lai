"""
Write a Python program that:    

a) Prompts the user to enter a number.    

b) Checks if the number is positive, negative, or zero.    

c) Prints an appropriate message based on the result.    
"""


### is_valid_f_number check if input is a floating number, return true or false 
def is_valid_f_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False
    
### infinite loop till a valid floating number is entered
while True:
    user_input=input('Enter a Number : ')

    if is_valid_f_number(user_input):
        print("Entry " + user_input + " is valid number " )
        number = float(user_input)
        break
    else:
        print("Entry " + user_input + " is Invalid! " )

if number < 0 :
    print(str(number) + " is less than 0")
elif number > 0:
    print(str(number) + " is greater than 0")
else :
    print(str(number) + " is zero")
