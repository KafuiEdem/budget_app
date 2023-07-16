class Category:

    

    #creating the constructor
    def __init__(self,item) -> None:
        self.item = item
        self.ledger =list()

    #building the deposit method
    def deposit(self,amount,description=""):
        deposit_item ={"deposit":{"amount":amount,"description":description}}
        name = {self.item:[deposit_item]}
        self.ledger.append(name)

    #buidling the withdraw method
    def withdraw(self,amount,description=""):
        for item in self.ledger:
            for key,value in item.items():
                if key == self.item:
                    for _,v in value[0].items():
                        if self.check_funds(amount) ==False:
                            pass
                        else:
                            # withdraw_amount = v["amount"] + amount
                            # print(withdraw_amount)
                            withdraw_item = {"withdraw":{"amount":-amount,"description":description}}

                            value.append(withdraw_item)  
                           

    #building the get_balance method
    def get_balance(self):
        deposit_amount = self.ledger[0][self.item][0].get("deposit")["amount"]
        withdrawal_amount = 0
        for entry in self.ledger[1:]:
            for key, value in entry.items():
                if "withdraw" in value:
                    withdrawal_amount += value["withdraw"]["amount"]
        balance_amount = deposit_amount + withdrawal_amount
        return {"balance": {"amount": balance_amount}}



    #building the the transfer method
    def transfer(self,amount,budget_item):
        for item in self.ledger:
            for key,value in item.items():
                if key == self.item:
                    # if value[0].get("deposit")["amount"] < amount:
                    if self.check_funds(amount) ==False:
                        pass
                    else:
                        transfer_to = {"transfer":{"amount":amount,"description":f"Transfer to {budget_item.item}"}}
                        value.append(transfer_to)
                        deposit_item ={"deposit":{"amount":amount,"description":f"Transfer from {key}"}}
                        name = {budget_item.item:[deposit_item]}
                        self.ledger.append(name)
                        
                 
    #building the check_funds method
    def check_funds(self,amount):
       if amount > self.get_balance().get("balance")["amount"]:
           return False
       else:
           return True
    #geting the output 
    def __str__(self) -> str:
        motd = f"{self.item:*^30}"
        items =""
        total = 0

        for item in self.ledger:
            for key,values in item.items():
                for value in values:
                    for description, amount in value.items():
                        for k,v in amount.items():
                            if "description" in k:
                                items +=f"\n{v[:23]:23}{amount['amount']:>7}"
                                total += amount["amount"]
        result = motd + items + "\nTotal: " +str(total)
        return result
    

def create_spend_chart(categories):
    pass

if __name__== "__main__":
  
  food = Category("Food")
  clothing = Category("Clothing")
  food.deposit(1000, "initial deposit")
  food.withdraw(10.15, "groceries")
  food.withdraw(15.89, "restaurant and more food for dessert")
  food.transfer(50, clothing)
  print(food)
#   print(food.get_balance())
    

