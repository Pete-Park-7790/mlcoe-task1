recipe = {
    "latte":{
        "ingredients":{
            "water" : 200,
            "sugar" : 100,
            "milk" : 200,
            "coffee" : 150,
        },
        "cost" : 200
    },

    "espresso":{
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 200,
            "coffee" : 200,
        },
        "cost" : 300
    },

    "cappuccino":{
        "ingredients":{
            "water" : 300,
            "sugar" : 150,
            "milk" : 400,
            "coffee" : 100,
        },
        "cost" : 400
    },
}

earning = 0

stock = {
    "water": 1000,
    "sugar": 1000,
    "milk": 1000,
    "coffee": 1000,
}

def main():
    global earning
    stat = input("Type 'On' to start the machine.\n")
    while stat.lower() == "on":
        choice = input("Select from a variety of options:\nLatte\nEspresso\nCappuccino\nStock\nAsset\nOff\n")

        if choice.lower() == "off":
            stat = "Off"
            print("Turning off the machine...\nHave a nice day... :)")

        elif choice.lower() == "asset":
            print(f"Asset: {earning}")

        elif choice.lower() == "stock":
            print(f"Water: {stock['water']} in ml")
            print(f"Sugar: {stock['sugar']} in g")
            print(f"Milk: {stock['milk']} in ml")
            print(f"Coffee: {stock['coffee']} in ml\n")

        else:
            coffee = recipe.get(choice.lower())
            if coffee:
                if resource_check(coffee['ingredients']):
                    money = int(input(f"Pay: {coffee['cost']}\n"))

                    if money >= coffee['cost']:
                        earning += coffee['cost']
                        print("Your payment is done... :)\n")
                        brewing(coffee['ingredients'])
                    else:
                        print("Not enough money. Transaction canceled.... :(")
            else:
                print("Invalid option. Please choose again..... :(")


def resource_check(requirements):
    for i in requirements:
        if requirements[i] > stock[i]:
            print(f"Oops,not sufficient.....{i}....:(")
            return False
    return True

def brewing(kaffee):
    for i in kaffee:
        stock[i] -= kaffee[i]
    print("Here is your Kaffee... :)\n\n")

main()