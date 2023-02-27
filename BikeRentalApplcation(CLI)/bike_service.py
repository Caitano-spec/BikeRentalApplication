import sys, os
import string
import random
import datetime


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('cls')
    
    print( """

                                                                                     
           Welcome to Mike Goodwin's Bike Service ,\n

    """)
    print( "Please choose the menu you want to start:")
    print( "1. Hire a Bike")
    print( "2. Bike Return")
    print( "3. Track My Progress")
    print( "\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print( "Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
            
    

# Menu 1
def menu1():
    global bike_type 
    global name
    global address
    
    print( "Bike Hire Menu !\n")

    print( "Customer Details !\n")

    try :
        name= input("Please Enter your name : ")
    except KeyboardInterrupt:
        print ("You have pressed the ctrl + c button.")
        menu1()
    
    
    print("\n") 
    address = input ("Please enter your address : ")
    print("\n")

    bike_type = input ("Please enter the type of Bike you would like : ")
    print("\n")
    
    print ("Select Booking Details to continue") 
    print ("5. Booking Details")
    print( "9. Back")
    print( "0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return



# Menu 2
def menu2():
    print( "Bike Return Menu !\n")

    e = datetime.datetime.now()

    print("Please enter your order number to return")

    reference_no = input()
    
    f = open("ordernumber.txt", "r")
    variable = f.readline()
    f.close()

    

    
    if reference_no != variable:
        print("Invalid Order No. Please Try Again")
        menu2()
    elif reference_no == variable:
        k = open("bike_return.txt", "r")
        print(k.read())
  

        print("Please Confirm if this is your receipt by typing : 'Yes' or 'No' ")
        return_receipt = input(" >> ") 
        if return_receipt.lower() in ['yes', 'no']:
             print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
             if e.hour == 10:
                  print("You have returned the bike at 10 am and so you will be charged £5 for each bike")
                  print ("Your deposit has been returned with deductions. Thank You for using our service.")
                  print("\n")
                  print ("1. Hire another Bike")
                  print( "9. Main Menu")
                  print( "0. Quit" )
                  choice = input(" >>  ")
                  exec_menu(choice)
                  return
             elif e.hour >10:
                 print("You are returning the Bike Late. So You will be charged the price of 1 day for each bike")
                 print ("Your deposit has has been returned with deductions. Thank You for using our service.")
                 print("---------------------------------------------------------------------")
                 print("\n")
                 print ("1. Hire another Bike")
                 print( "9. Main Menu")
                 print( "0. Quit" )
                 choice = input(" >>  ")
                 exec_menu(choice)
                 return
             else:
                print("Thank You for returning your bike. Your full deposit has been returned.")
                print ("1. Hire another Bike")
                print( "9. Main Menu")
                print( "0. Quit" )
                choice = input(" >>  ")
                exec_menu(choice)
                return               
            
        else:
            print("Invalid Input. Please Try Again")
            menu2() 
    


def menu3():
    print( "Track Your Progress !\n")
    print("Welcome...")
    welcome = input("Do you have an acount? y/n: ")

    if welcome == "n":
     while True:
        print ("REGISTER NOW") 
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do NOT match!")
    if welcome == "y":
     while True:
        print ("LOGIN")
        
        login1 = input("Username:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome")
            print("Your Weekly Cycle Activities")
            print("Please select what you would like to do next ")
            print("12. View My Log") 
            print( "8. Add")
            print("11. Delete") 
            print( "0. Exit" )
            choice = input(" >>  ")
            exec_menu(choice)
            return
                         
            
            break 
        print("Incorrect username or password.")
 
    
    
    print( "9. Main Menu")
    print( "0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()



           

def hiredetails():
    global adultcost
    global childcost 
    adultcost = 18 # adilt cot 
    childcost = 9  #kids price 
    global adult_deposit
    global child_deposit  
    global child
    global adults
    global total
    global days
    global adult_price
    global child_price
    
    while True :
         try:
             adults = int(input ("Please Enter the Number of Adult Bikes you would like to hire : "))
             print("\n")
             break 
         except :
                print ("INvalid Input")
                print("\n")
        
    if adults <=0 :
        print("------------------------------------------------------------------------------")
        print("Number of Adult Bikes has to be min 1. 0 or Negative values cannot be entered. ")
        print("\n")
        print("NOTE : * You have to be an Adult to hire a bike. Unaccompanied Children Cannot Hire Bikes ")
        print("\n")
        print("Please Try Again.")
        print("------------------------------------------------------------------------------")
        print("\n")
        hiredetails()
   
    if adults > 0:
        max_child = adults * 3
        while True :
            try:
                child = int(input ("Enter the Number of Children Bike you would like to hire :" ))
                print("\n")
                break 
            except:
                 print ("You can only input integers. Please try again ")
                 print("\n")
                 
        if child > max_child:
            print("------------------------------------------------------------------------------")
            print ("* NOTE: There must be no more than 3 children per adult, to ensure safety. Thanks")
            print("\n")
            print ("Please Try Again")
            print("------------------------------------------------------------------------------")
            print("\n")
            print("\n")
            hiredetails()
        if child < 0:
            print ("Negative Values Cannot be Entered. Please Try Again")
            print("\n")
            hiredetails()
        elif child ==0:
            while True:
                try:
                    days = int(input("Enter the number of days you would like to rent the bike"))
                    print("\n")
                    break 
                except:
                    print ("The Number of Days entered is invalid. Ensure you enter the number as integer.")
                    print("\n")
            if days <= 0:
                print("0 or Negative values cannot be entered. Number of days have to be greater than 0")
                print("\n")
                adultbike()
            else:
                print("\n")
                adult_deposit = adults * 100
                print ("You have to pay a returnable deposit of £{} for the adult bikes".format(adult_deposit))
                adult_price = adults * adultcost * days 
                total = (adult_price + adult_deposit)
                print("You have rented {} adult bike(s) for {} day(s)".format(adults, days))
                print("You have to pay £{} for the adult bikes(s) excluding returnable deposit".format(adult_price))
                print("Your total will be £{} including returnable deposit".format(total) )
                print("\n")
                
            
        else:
            while True:
                try:
                    days = int(input("Enter the number of days you would like to rent the bike"))
                    print("\n")
                    break
                except:
                    print ("The Number of Days entered is invalid. Ensure you enter the number as integer.")
                    print("\n")
            if days <=0:
                print("0 or Negative values cannot be entered. Number of days have to be greater than 0")
                print("\n")
                hiredetails()
            else:
                adult_deposit = adults * 100
                child_deposit = child * 70
                print ("You have to pay a returnable deposit of £{} for the adult bikes and £{} for the child bikes".format(adult_deposit, child_deposit))
                adult_price = adults * adultcost * days
                child_price = child * childcost * days 
                total = (adult_price + adult_deposit) + (child_price + child_deposit)
                print("You have rented {} adult bike(s) and {} child bike(s) for {} day(s)".format(adults, child, days))
                print("You have to pay £{} for the adult bikes(s) + £{} for the child bike(s) excluding returnable deposit".format(adult_price, child_price))
                print("Your total will be £{} including returnable deposit".format(total) )
                print("\n")
    print ("Please Select What you would like to do next :")
    print( "6. Checkout")
    print( "9. Back")
    print( "0. Exit") 
    choice = input(" >>  ")
    exec_menu(choice)
    return
            
def checkout():

    print ("Please Enter One of the Following Payment Methods : 'Cash' , 'Cheque' or  'Card' ")
    payment_method = input (" >>  ")
    if payment_method.lower() in['cash', 'cheque']:
        print ("Choose Pay Now to Complete Your Payment and to Confirm your order")
        print ("7. Pay Now")
        print ("0. Exit")
        choice = input(" >>  ")
        exec_menu(choice)
        return

    elif payment_method.lower() in['card']:
        print ("Please Enter Your Card Type : 'Master' , 'Visa' or  'Delta' ")
        card_type = input(" >> ") 
        if card_type.lower() in ['master', 'visa', 'delta']:
            print("Choose Pay Now to Complete Your Payment and to Confirm your order")
            print ("7. Pay Now")
            print ("0. Exit")
            choice = input(" >>  ")
            exec_menu(choice)
            return
        else:
            print("Invalid Card Type. Please Try Again.")
            checkout()
    else:
        print("Invalid Payment Method. Please Try Again.")
        checkout()
def order_confirmation():
    global order_no
    global total_deposit 
    print("Payment Successful !!! ")
    print("\n")
    print("\n")
    print("-----------------------------------------------")
    print("      ORDER CONFIRMATION                       ")
    print("-----------------------------------------------")
    order_no = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print("Your order No : {}.".format(order_no))
    print("-----------------------------------------------")
    print("\n")
    print("Name : {}  ".format(name))
    print("Address: {} .".format(address))
    print("-----------------------------------------------")
    print("Bike Type : {} | Category : ADULT | Quantity : {} | Duration : {} | Total : {} |".format(bike_type, adults, days, adult_price))

    
    if child == 0:
        total_deposit = adult_deposit
        
    else:
        total_deposit = adult_deposit + child_deposit 
    
    if child != 0:
          print("Bike Type : {} | Category : CHILD | Quantity : {} | Duration : {} | Total : {} |".format(bike_type, child, days, child_price))
    print("DEPOSIT : {} ".format(total_deposit))
    print("Total : {}".format(total))
    print("Thank you for hiring with us.")
    print("*NOTE: Please Use the exact order number as displayed while returning your Bike")

    #stores order number in text file.       
    k = open("ordernumber.txt", "w")
    k.write(order_no)
    k.close()

    k = open("bike_return.txt", "w")
    k.write("\n")
    k.write("\n")
    k.write("---------------------------------------------------------------")
    k.write("\n")
    k.write("Thank You For Returning Your Bike")
    k.write("\n")
    k.write("---------------------------------------------------------------")
    k.write ("\n")
    k.write("Name : {} ".format(name))
    k.write ("\n")
    k.write ("\n")
    k.write("Address: {} ".format(address))
    k.write ("\n")
    k.write ("\n")
    k.write("Bike Type: {} ".format(bike_type))
    k.write ("\n")
    k.write ("\n")
    k.write ("You have purchased {} adult bikes and {} child bikes for {} days from us.".format(adults, child, days))
    k.write ("\n")
    k.write ("\n")
    k.write("You have paid a total deposit of £ {}".format(total_deposit))
    k.write ("\n")
    k.write ("\n")
    k.write("You have paid a total of £{}".format(total))
    k.write ("\n")
    k.write("---------------------------------------------------------------")
    
    k.close()



    if (1500 <=total<=10000):
        print("\n")
        print("\n")
        print ("--------------------------------------------")
        print("LOAN QUOTE")
        print("\n")
        print ("--------------------------------------------")
        print("You are eligible for a loan of £{}".format(total))
        print("You will be charged @ 3.8% interest over 3-5 years")
        print ("--------------------------------------------")
        P = total #loan amount
        r = 3.8 # interest rate of 3.8%
        n = 1 # compounded once per year
        t = 3#3 years time span.
        A = P * (((1 + ((r/100.0)/n)) ** (n*t)))
        print ("The final amount after 3 years will be £{}".format(A))
        t = 4 # 4 years
        A = P * (((1 + ((r/100.0)/n)) ** (n*t)))
        print ("--------------------------------------------")
        print ("The final amount after 4 years will be £{}".format(A))
        t = 5 # 5 years 
        A = P * (((1 + ((r/100.0)/n)) ** (n*t)))
        print ("--------------------------------------------")
        print ("The final amount after 5 years will be £{}".format(A))
        print("\n")
        print("1. Hire another Bike")
        print( "2. Return a Bike")
        print( "0. Exit") 
        choice = input(" >>  ")
        exec_menu(choice)
        return
    else:
        print("1. Hire another Bike")
        print( "2. Return a Bike")
        print( "0. Exit") 
        choice = input(" >>  ")
        exec_menu(choice)
        return

    
def add():
    
    f = open("ordernumber.txt", "r")
    variable = f.readline()
    f.close()
    reference_no = input("Please enter your recent order_no to log your activity")


    if reference_no == variable:
        dateinput = input ("Please enter the date you have driven the bike")
        duration = input("Please enter for how long you have driven the bike")
        s = open("mylog.txt", "a")
        s.write("\n") 
        s.write("MY PROGRESS LOG")
        s.write("\n") 
        s.write("------------------------------") 
        s.write("\n") 
        s.write(dateinput + ":" + duration)
        s.write("\n")
        s.close()
        print("3. Track My Progress - Main Menu ")
        print("12. view my log ")
        print( "11. Delete previous log")
        print( "0. Exit") 
        choice = input(" >>  ")
        exec_menu(choice)
        return
    else:
        print("Invalid Order Number")
        menu3() 
    



def delete():
    with open('mylog.txt') as f1:
        lines = f1.readlines()

    with open('mylog.txt', 'w') as f2:
        f2.writelines(lines[:-4])

    print("You have successfully deleted your last log")
    print("\n") 
    print("2. Track My Progress - Main Menu ")
    print("8. add to my log ")
    print( "12. view my log")
    print( "0. Exit") 
    choice = input(" >>  ")
    exec_menu(choice)
    return
    
    
    
def view():
    
    try:
         s = open("mylog.txt", "r")
         print(s.read())   
        
    except FileNotFoundError :
        print ( "Your log is empty. You have to add something in your log to get started")
    
        
     
    print("3. Track My Progress - Main Menu ")
    print("8. add to my log ")
    print( "11. Delete previous log")
    print( "0. Exit") 
    choice = input(" >>  ")
    exec_menu(choice)
    return





# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,##hire a bike
    '2': menu2,##return a bike
    '3': menu3,##track my progresss
    '5': hiredetails,
    '6': checkout,
    '7': order_confirmation,
    '8': add,
    '11': delete,
    '12': view,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()

