"""

Write a program that:    

a) Prompts the user to input an integer nnn.    

b) Uses a for loop to print all even numbers from 1 up to nnn.    

c) Ensures only even numbers appear in the output.   

"""

### is_valid_int check if input is a integer, return true or false 
def is_valid_int(input_string):
    try:
        if int(input_string) > 0:
            return True
        else:
            return False
            
    except ValueError:
        return False
    
### infinite loop till a valid floating number is entered
while True:
    user_input=input('Enter a Number Grater than 0: ')

    if is_valid_int(user_input):
        print(f"Entry {user_input}  is valid number " )
        number = int(user_input)
        break
    else:
        print(f"Entry {user_input}  is Invalid! " )


for i in range (1,number):
    if i%2 == 0:
        print(i)
