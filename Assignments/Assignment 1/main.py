### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Loops through the ingredients in the resources dictionary
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # Prompting to ask the user to enter a combination of coins 
        # Initialize the different coins followed by asking the user to enter each amount in the prompt
        print("Please insert coins.")
        larges = int(input("How many large dollars?: "))
        halfs = int(input("How many half dollars?: "))
        quarters = int(input("How many quarter dollars?: "))
        nickels = int(input("How many nickels?: "))
        
        # The total variable is used to add all the combinations of coins as well as multiplying the coins based on their specific amount then returning the total 
        total = larges * 1 + halfs * 0.5 + quarters * 0.25 + nickels * 0.05
        return total
           
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # if the users coins are equal or more than the cost, the user will recieve change back based on the different of the two. Otherwise it will return false if the user doesn't have enough the pay
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enoguh money. Money refunded. ")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        # Defining the ingredients and cost variable to retrieve what the user ordered to get the amount of ingredients needed + cost 
        ingredients = recipes[sandwich_size]['ingredients']
        cost = recipes[sandwich_size]['cost']
        
        # Checks the amount of resources assign coins to call the process coins function
        # If the transaction is successful loop through the resources needed to make the sandwich. Otherwise there are not enough resources
        if self.check_resources(ingredients):
            coins = self.process_coins()
            if self.transaction_result(coins, cost):
                for item, amount in ingredients.items():
                    self.machine_resources[item] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")
            else:
                print("Sorry there aren't enough resources to make the sandwich.")

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)



while True:
    # The prompt is presented to the user to make a choice from the options
    print("What would you like? (small/ medium/ large/ off/ report): ")
    choice = input().lower()
    # The prgoram ends if the user types off
    if choice == "off":
        print("The machine is turning off.")
        break
    # Gives a report of resources by looping through the items in the resources 
    elif choice == "report":
        for item, amount in resources.items():
            print(f"{item.capitalize()}: {amount}")
    # If any of the size sandwiches are chosen, it will order ingredients from resources then makes the sandwich from the make sandwich function called
    elif choice in ["small", "medium", "large"]:
          sandwich_size = choice
          order_ingredients = recipes[sandwich_size]['ingredients']
          sandwich_machine.make_sandwich(sandwich_size, order_ingredients)
    # Prompts the user the enter a valid input only based on the options provided
    else:
        print("Please enter a valid input")
             