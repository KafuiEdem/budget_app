class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []

    #setting the deposit method
    def deposit(self, amount, description=""):
        deposit_item = {"amount": amount, "description": description}
        self.ledger.append(deposit_item)

    #setting the withdarw method
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            withdrawal_item = {"amount": -amount, "description": description}
            self.ledger.append(withdrawal_item)
            return True
        else:
            return False
        
    #setting the get balance method
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            if "amount" in entry:
                balance += entry["amount"]
        return balance
    
    #setting the check funds method 
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    #setting the transfer method
    def transfer(self, amount, budget_item):
        if self.check_funds(amount):
            transfer_item = {"amount": -amount, "description": f"Transfer to {budget_item.item}"}
            deposit_item = {"amount": amount, "description": f"Transfer from {self.item}"}
            self.ledger.append(transfer_item)
            budget_item.ledger.append(deposit_item)
            return True
        else:
            return False

    #setting the the __str__ method for the output
    def __str__(self):
        motd = f"{self.item:*^30}"
        items = ""
        total = 0

        for entry in self.ledger:
            if "description" in entry:
                description = entry["description"]
                amount = entry["amount"]
                items += f"\n{description[:23]:23}{amount:>7.2f}"
                total += amount

        result = motd + items + f"\nTotal: {total:.2f}"
        return result

def create_spend_chart(categories):
    # Calculate the total spent for each category
    total_spent = {}
    for category in categories:
        total_spent[category.item] = sum(
            entry["amount"]
            for entry in category.ledger if entry.get("amount",0) < 0
        )

    # Calculate the percentage spent for each category
    percentages = {}
    total = sum(total_spent.values())
    for category, spent in total_spent.items():
        percentage = spent / total * 100
        percentages[category] = percentage

    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages.values():
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    # Find the longest category name
    max_name_length = max(len(category.item) for category in categories)

    # Add category names to the chart
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.item):
                chart += f"{category.item[i]}  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


"""
    I have to run the test items to see where the error is.
    The difficult part of this project is the transfer method.
    This method was behaving very funny, but i manage to fix it.
"""
# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("business")


# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# c=create_spend_chart([business, food, entertainment])
# print(c)

# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()


# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()
# food.ledger[2]
# # print(food)

# transfer_amount = 20
# good_transfer = food.transfer(transfer_amount, entertainment)
# actual_ledger_item = food.ledger[-1]  # Get the last item in the ledger
# expected_ledger_item = {
#     "transfer": {"amount": -20, "description": f"Transfer to {entertainment.item}"}
# }
# print("Actual ledger item:", actual_ledger_item)
# print("Expected ledger item:", expected_ledger_item)
