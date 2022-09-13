print("Welcome to Compound Interest Calculator")
A = int(input("Please enter the future value of the investment/loan, including interest :   "))# this takes in an integer input from the user
try:
    P = int (input(" Please enter the principal amount(the initial deposit or loan amount):   "))
except:
    print("You can only enter integers")
r = float(input("Please enter the annual interest rate:  "))# this takes in float input from the user.
n = int(input("Please enter the number of times that the interest is compounded per year:  "))
t = 3 
A = P * (((1 + ((r/100.0)/n)) ** (n*t)))# this is the formula for calculating annual compound interest. 
print ("The final amount after 3 years is", A)#This displays the final amount of the compound interest.
t = 4 
A = P * (((1 + ((r/100.0)/n)) ** (n*t)))# this is the formula for calculating annual compound interest.
print ("The final amount after 4  years is", A)#This displays the final amount of the compound interest.
t = 20
A = P * (((1 + ((r/100.0)/n)) ** (n*t)))# this is the formula for calculating annual compound interest.
print ("The final amount after 5  years is", A)#This displays the final amount of the compound interest.

