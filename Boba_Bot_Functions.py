import string 
import random
import nltk

your_total = 0

def greet_customer():
    """ Main function to activate Boba Bot. """
    response = input("Welcome! Would you like to order? \
            \nEnter yes or no. \n\t")
    
    #Carries out the first ordering function if user wants to order
    if response.lower() == "yes":
        choose_base()
        
    #Ends bot if user doesn't want to order
    elif response.lower() == "no":
        print("Okay, see you next time!\n")
    #Guides user to type program recognized input     
    else:
        response = input("Please enter yes or no.\n\t")
        greet_customer()

        
def choose_base():
    """ Asks user for input and checks if input is in a list
    
        This function must run in order to proceed into next function.
    
    """
    base_choice = input("Pick a base: green, black, " + \
        "milk, oolong, or matcha.\n\t")
    
    tea_base = ['green', 'black', 'milk', 'oolong',
        'matcha'] 
    
    #Proceeds with order if user input matches item on menu
    if base_choice.lower() in tea_base:
        choose_flavor()
    
    #Prompts user to type program recognized input
    else:
        base_choice = input("Sorry, that is not an option. " + \
        "Type 'base' to see options.\n\t")
        
        #Gives user string with options that belong to the specified list 
        while base_choice.lower() == "base":
            choose_base()
            break
            

def choose_flavor():
    """ Asks user for input and checks if input is in assigned list"""
    
    flavor_choice = input("Pick a flavor: strawberry, " + \
            "lychee, mango, or wintermelon.\n\t")
    
    tea_flavor = ['strawberry', 'lychee', 'mango', 
        'wintermelon']
    
    #Gives user option to edit input
    if flavor_choice.lower() in tea_flavor:
        flavor_choice = input("Is this the flavor you want?\n\t")
        if flavor_choice.lower() == "yes":
            topping_or_not()    
        else:
            choose_flavor()
            
    #Prompts user to input an item 
    #from specified list so order can proceed
    else:
        print("Sorry, that is not an option.\n\t")
        choose_flavor()
        

def topping_or_not():
    """ Checks if input is needed"""
    optional_topping = input("Would you like to add a " + \
            "topping to your drink? \nEnter yes or no.\n\t")
    
    toppings = {'honey boba': .5, 'aloe': .5, 
        'lychee jelly': .5, 'grass jelly': .5, 
        'mochi balls': .75, 'crystal boba': .75, 
        'milk foam': .75}
    
    #Extends price from 
    #global namespace to local namespace
    global your_total
    
    #Prints items from specified list if user wants to order a topping
    if optional_topping.lower() == "yes":
        print("These are your options:\n\t")
        for key in toppings:
            print("- " + key)
        choose_topping()
    
    #Asks user to choose sugar level when done with adding toppings
    else:
        choose_sugar()


def add_topping():
    """ Checks if additional input is needed"""
    
    more_topping = input("Would you like to add another " + \
            "topping?\n\t")
    
    #Gives user option to add more toppings 
    if more_topping.lower() == "yes":
        choose_topping()
    elif more_topping.lower() == 'no':
        choose_sugar()
    else:
        print('Invalid entry. Try again.')
        add_topping()

toppings = {'honey boba': .5, 'aloe': .5, 
           'lychee jelly': .5, 'grass jelly': .5, 
        'mochi balls': .75, 'crystal boba': .75, 
        'milk foam': .75}
basic_toppings = ['honey boba', 'aloe', 'lychee jelly', 'grass jelly']
premium_toppings = ['mochi balls', 'crystal boba', 
        'milk foam']
        
def choose_topping():
    """Asks user for input 
    
       Execution of this function is 
       a requirement to run next function
    """
    
    global your_total
    
    #Asks user to choose a topping 
    topping_choice = input("Which topping would you " + \
            "like to add?\n\t")
    
    toppings = {'honey boba': .5, 'aloe': .5, 
        'lychee jelly': .5, 'grass jelly': .5, 
        'mochi balls': .75, 'crystal boba': .75, 
        'milk foam': .75}
    
    basic_toppings = ['honey boba', 'aloe', 'lychee jelly', 'grass jelly']
    
    premium_toppings = ['mochi balls', 'crystal boba', 
        'milk foam']
   
    
    #Checks if user's input is a topping on the menu or not
    if topping_choice.lower() in toppings:
        
        #Adds price of topping to total price 
        if topping_choice.lower() in basic_toppings:
            print("Okay, that will be $0.50.")
            your_total += .5
            add_topping()

        if topping_choice.lower() in premium_toppings:
            print("Okay, that will be $0.75.")            
            your_total += .75
            add_topping()
    
    #Asks user to choose a new topping 
    #if their input is not a topping on the menu  
    else:
        topping_choice = input("Topping unavailable.\n\t")
        topping_or_not()

        
def choose_sugar():
    """ Asks user for input
    
        Execution of this function is 
        a requirement to run next function  
    """
    
    #Asks user if they want to adjust drink sweetness
    sugar_level = input("Would you like to adjust your" + \
            " sugar level? \nEnter yes or no.\n\t")
    
    sugar = ['extra', 'half', 'quarter', 'zero']
    
    #Asks user to input desired drink sweetness
    if sugar_level.lower() == "yes":
        sugar_level = input("Choose your preference:" + \
                " extra, half, quarter, or zero.\n\t")
        
        #Checks if user's desired sweetness is on the menu 
        if sugar_level.lower() in sugar:
            sugar_level = input("Continue?\n\t")
            if sugar_level.lower() == "yes":
                choose_ice()
            else: 
                choose_sugar()
        
        #Displays acceptable sugar levels 
        #if user's input is not on the menu
        else:
            sugar_level = input("Sorry, that is not an" + \
            " option. \nPlease choose either: extra," + \
            " half, quarter, or zero.\n\t")
    else:
        choose_ice()

        
def choose_ice():
    """ Asks user for input
    
        Execution of this function is 
        a requirement to run next function  
    """
    
    #Asks user if they want to adjust ice level
    ice_level = input("Would you like to adjust your" + \
            " ice level? \nEnter yes or no.\n\t")
    
    ice = ['extra', 'light', 'zero']
    
    #Asks user to input desired ice level
    if ice_level.lower() == "yes":
        ice_level = input("Choose your preference:" + \
                " extra, light, or zero.\n\t")
        
        #Checks if user's desired ice level is on the menu
        if ice_level.lower() in ice:
            ice_level = input("Continue?\n\t")
            if ice_level.lower() == "yes":
                choose_size()
            else:
                choose_ice()
        
        #Displays acceptable ice levels 
        #if user's input is not on the menu
        else:
            ice_level = input("Sorry, that is not an" + \
                    " option. Please choose either:" + \
                    " extra, light, or zero.\n\t")
    else:
        choose_size() 
        
        
def choose_size():
    """Asks for user input 
    
       Execution of this function is 
       a requirement to run next function 
    """
    
    #Extends price from global namespace to local namespace
    global your_total
    
    #Asks user to choose a drink size
    cup_size = input("Would you like a regular or" + \
            " large size?\n\t")
    
    cup = ['regular', 'large']
    
    #Adds price of cup to total price
    while cup_size in cup:
        if cup_size.lower() == "regular":
            your_total += 4
        elif cup_size.lower() == "large":
            print("Size upgrade will be an additional $0.50.")
            your_total += 4.5
        break
        
    #Asks user to re-enter size 
    #if first input is not a size on the menu 
    while cup_size not in cup:
        cup_size = input("Please choose either regular" + \
                " or large.\n\t")
        break
    order_more()
    
    
def order_more():
    """ Restarts ordering system 
    
    """
    
    #Asks user if they want to order another drink
    cont = input("Would you like to order anything" + \
            " else? Enter yes or no.\n\t")
    
    if cont.lower() == "yes":
        choose_base()
        
    #Tells user how much they need to pay
    else:
        calculate_price()
        
        
def calculate_price():
    """Calculates total price based on user's inputs
    
    """
    
    global your_total
    tax = 0.0775*your_total
    
    #Assigns user's total to new variable
    your_total = your_total + tax
    you_pay = your_total
    print("Amount due = ${0:.2f}".format(you_pay))
    print("\nThank you!")
    
    
def check_wallet(wallet, total):
    """ Checks if user has enough money
    
    Parameters:
        wallet (int): Amount user has in wallet
        total (int): Amount user needs to pay 
    """
    global your_total
    if wallet >= total:
        print('Great! You have enough money.')
    else:
        print('Uh oh! You do not have enough money.')
        
    your_total = 0
        
def need_straw():
    """Checks if user wants a straw
    """
    ans = input('Do you need a straw?\n\t')
    msg = ans.lower()
    if ans.lower() == 'yes':
        print('Here you go.')
    elif ans.lower() == 'no':
        print('\nOkay, have a good day!')
    else:
        print('\nInvalid response.') 