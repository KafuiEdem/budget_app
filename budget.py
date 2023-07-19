class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []

    def deposit(self, amount, description=""):
        deposit_item = {"amount": amount, "description": description}
        self.ledger.append(deposit_item)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            withdrawal_item = {"amount": -amount, "description": description}
            self.ledger.append(withdrawal_item)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            if "amount" in entry:
                balance += entry["amount"]
        return balance
    

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def transfer(self, amount, budget_item):
        if self.check_funds(amount):
            transfer_to = {"transfer": {"amount": -amount, "description": f"Transfer to {budget_item.item}"}}
            self.ledger.append(transfer_to)
            deposit_item = {"deposit": {"amount": amount, "description": f"Transfer from {self.item}"}}
            budget_item.ledger.append(deposit_item)
            return True
        else:
            return False

    def __str__(self):
        motd = f"{self.item:*^30}"
        items = ""
        total = 0

        for entry in self.ledger:
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
            for entry in category.ledger
            if entry["amount"] < 0
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



food = Category("Food")
entertainment = Category("Entertainment")
business = Category("business")


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
c=create_spend_chart([business, food, entertainment])
print(c)

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
transfer_amount = 20
food_balance_before = food.get_balance()
entertainment_balance_before = entertainment.get_balance()
good_transfer = food.transfer(transfer_amount, entertainment)
food_balance_after = food.get_balance()
entertainment_balance_after = entertainment.get_balance()


food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
transfer_amount = 20
food_balance_before = food.get_balance()
entertainment_balance_before = entertainment.get_balance()
good_transfer = food.transfer(transfer_amount, entertainment)
food_balance_after = food.get_balance()
entertainment_balance_after = entertainment.get_balance()
food.ledger[2]
# print(food)