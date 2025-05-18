"""
a) Declares variables for storing a user’s name, age, and height. 

b) Prints a greeting message using the name. 

c) Calculates the user’s age 10 years from now. 

d) Displays height in meters by converting height from centimetres. 

"""

### Declares variables for storing a user’s name, age, and height. 

name = "Lai KwaiSeng"
age = "56"
height = "185"

### Prints a greeting message using the name. 

print("Hello " + name)

age_10yrs_later = int(age) + 10
print("You will be  " + str(age_10yrs_later) + " in 10 years time")

metric_heigh_in_m = int(height)/100

print("Your height it " + str(metric_heigh_in_m) + "M")