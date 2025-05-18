'''
Write a program that:    

a) Defines a function to calculate the area of a rectangle using length and width as inputs.    

b) Prompts the user to input values for length and width.    

c) Calls the function to calculate and then displays the area in a formatted message.    
'''

### a function to return the area of rectangle
### acceots length and height as floating number

def  area_of_rectangle(length,height):
    return length*height

### is_valid_f_number check if input is a +ve floating number, return true or false 
def is_valid_f_number(input_string):
    try:
        if float(input_string) > 0:
            return True
        else:
            return False
        
    except ValueError:
        return False
    
### infinite loop till a valid Length  is entered
while True:
    user_input_length=input('Enter  Length : ')

    if is_valid_f_number(user_input_length):
        print(f"Valid Length : {user_input_length } " )
        length = float(user_input_length)
        break
    else:
        print(f"Invalid Length  { user_input_length}! " )

### infinite loop till a valid Width  is entered
while True:
    user_input_heigth=input('Enter  Width : ')

    if is_valid_f_number(user_input_heigth):
        print(f"Valid Length : {user_input_heigth } " )
        height = float(user_input_heigth)
        break
    else:
        print(f"Invalid Length  { user_input_heigth}! " )

# print area to 2 decimal value

print(f"Area = {round(area_of_rectangle(length,height),2)}")
