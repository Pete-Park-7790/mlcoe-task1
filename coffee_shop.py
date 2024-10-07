# Dictionary containing recipes for different types of coffee
recipe = {
    "latte":{   # Latte recipe and cost
        "ingredients":{
            "water" : 200,
            "sugar" : 100,
            "milk" : 200,
            "coffee" : 150,
        },
        "cost" : 200
    },

    "espresso":{    # Espresso recipe and cost
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 200,
            "coffee" : 200,
        },
        "cost" : 300
    },

    "cappuccino":{    # Cappuccino recipe and cost
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 400,
            "coffee" : 100,
        },
        "cost" : 400
    },
}

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
DEEP = "\033[38;5;160m"
GOLD = "\033[38;5;214m"
ORANGE = "\033[38;5;202m"
RESET = "\033[0m" 
DARK = "\033[31m"
MUSTARD = "\033[38;5;190m"



# Variable to track total earnings
earning = 0

# Stock of ingredients
stock = {
    "water": 1000,
    "sugar": 1000,
    "milk": 1000,
    "coffee": 1000,
}

# Main function to start and control the coffee machine
def main():
    global earning      
    stat = input(f"{YELLOW}Type {DEEP}'On'{YELLOW} to start the machine.\n{DEEP}")   # Ask user to turn on the machine
    # Loop continues as long as the machine is 'On'
    while stat.lower() == "on":

        # Ask user to choose an option from the menu
        choice = input(f"{YELLOW}Select from a variety of options:{RED}\nLatte\nEspresso\nCappuccino\nStock\nAsset\nOff\n\n{MUSTARD}")

        if choice.lower() == "off":     # If user chooses 'Off', stop the machine
            stat = "Off"
            print(f"{ORANGE}Turning off the machine...\nHave a nice day... :)\n{RESET}")

        elif choice.lower() == "asset":     # If user chooses 'Asset', display total earnings
            print(f"{GOLD}Asset: {earning}\n{RESET}")

        elif choice.lower() == "stock":     # If user chooses 'Stock', display available stock
            print(f"{BLUE}Water: {stock['water']} in ml{RESET}")
            print(f"Sugar: {stock['sugar']} in g")
            print(f"{DARK}Coffee: {stock['coffee']} in ml{RESET}")
            print(f"Milk: {stock['milk']} in ml\n")

        else:    
            coffee = recipe.get(choice.lower())
            if coffee:      # If user selects a valid coffee option

                # Check if there are enough ingredients to make the coffee
                if resource_check(coffee['ingredients']):
                    money = int(input(f"{GOLD}Pay: {coffee['cost']}\n{MUSTARD}"))    # Ask user to pay the required amount

                    if money >= coffee['cost']: # If enough money is paid
                        earning += coffee['cost'] # Add the money to the earnings
                        print(f"{DEEP}Your payment is done... :)\n{RESET}")
                        brewing(coffee['ingredients']) # Brew the coffee
                    else:
                        print(f"{GREEN}Not enough money. Transaction canceled.... :(\n{RESET}")
            else:
                print(f"{GREEN}Invalid option. Please choose again...{RESET}")

# Check if stock is sufficient
def resource_check(requirements):
    for i in requirements:
        if requirements[i] > stock[i]:
            print(f"{GREEN}Oops,not sufficient.....{i}....:({RESET}")
            return False
    return True

# Function to brew the coffee and update stock
def brewing(kaffee):
    for i in kaffee:
        stock[i] -= kaffee[i]
    print(f"{GOLD}Here is your {ORANGE}Kaffee{GOLD}... :)\n{RESET}")

# Start the coffee machine
main()