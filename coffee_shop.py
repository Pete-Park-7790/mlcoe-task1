# Dictionary containing recipes for different types of coffee
recipe = {
    "latte":{   # Latte recipe with ingredients and cost
        "ingredients":{
            "water" : 200,
            "sugar" : 100,
            "milk" : 200,
            "coffee" : 150,
        },
        "cost" : 200
    },

    "espresso":{    # Espresso recipe with ingredients and cost
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 200,
            "coffee" : 200,
        },
        "cost" : 300
    },

    "cappuccino":{    # Cappuccino recipe with ingredients and cost
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 400,
            "coffee" : 100,
        },
        "cost" : 400
    },
}

# Variable to track total earnings
earning = 0

# Initial stock of ingredients
stock = {
    "water": 1000,
    "sugar": 1000,
    "milk": 1000,
    "coffee": 1000,
}

# Main function to start and control the coffee machine
def main():
    global earning      
    stat = input("Type 'On' to start the machine.\n")   # Ask user to turn on the machine

    # Loop continues as long as the machine is 'On'
    while stat.lower() == "on":

        # Ask user to choose an option from the menu
        choice = input("Select from a variety of options:\nLatte\nEspresso\nCappuccino\nStock\nAsset\nOff\n")

        if choice.lower() == "off":     # If user chooses 'Off', stop the machine
            stat = "Off"
            print("Turning off the machine...\nHave a nice day... :)")

        elif choice.lower() == "asset":     # If user chooses 'Asset', display total earnings
            print(f"Asset: {earning}")

        elif choice.lower() == "stock":     # If user chooses 'Stock', display available stock
            print(f"Water: {stock['water']} in ml")
            print(f"Sugar: {stock['sugar']} in g")
            print(f"Milk: {stock['milk']} in ml")
            print(f"Coffee: {stock['coffee']} in ml\n")

        else:    
            coffee = recipe.get(choice.lower())
            if coffee:      # If user selects a valid coffee option

                # Check if there are enough ingredients to make the coffee
                if resource_check(coffee['ingredients']):
                    money = int(input(f"Pay: {coffee['cost']}\n"))    # Ask user to pay the required amount

                    if money >= coffee['cost']: # If enough money is paid
                        earning += coffee['cost'] # Add the money to the earnings
                        print("Your payment is done... :)\n")
                        brewing(coffee['ingredients']) # Brew the coffee
                    else:
                        print("Not enough money. Transaction canceled.... :(")
            else:
                print("Invalid option. Please choose again..... :(")

# Check if stock is sufficient
def resource_check(requirements):
    for i in requirements:
        if requirements[i] > stock[i]:
            print(f"Oops,not sufficient.....{i}....:(")
            return False
    return True

# Function to brew the coffee and update stock
def brewing(kaffee):
    for i in kaffee:
        stock[i] -= kaffee[i]
    print("Here is your Kaffee... :)\n\n")

# Start the coffee machine
main()