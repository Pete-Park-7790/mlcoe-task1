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
    stat = input("Type 'On' to start the machine.")
    while stat.lower == "on":
        choice = input("Select from a variety of options:\nLatte\nEspresso\nCappuccino\nStock\nAsset\nOff\n")

        if choice.lower == "off":
            stat = "Off"
            print("Turning off the machine...\nHave a nice day...")

        elif choice.lower == "asset":
            print(f"Asset: {earning}")

        elif choice.lower == "stock":
            print(f"Water: {stock['water']}in ml")
            print(f"Sugar: {stock['sugar']}in g")
            print(f"Milk: {stock['milk']}in ml")
            print(f"Coffee: {stock['coffee']}in ml")

        else:
            coffee == recipe[choice.lower]
            if resource_check(coffee['ingredients']):
                money = input(print(f"Pay: {recipe['cost']}"))
                earning += money
                print("Your payment is done")
                brewing(coffee['ingredients'])


def resource_check(requirements):
    
    
def brewing(kaffee):
    


main()