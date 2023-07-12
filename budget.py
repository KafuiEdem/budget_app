class Category:

    ledger =list()

    #creating the constructor
    def __init__(self,item) -> None:
        self.item = item

    #building the deposit method
    def deposit(self,amount,description=""):
        deposit_item ={"deposit":{"amount":amount,"description":description}}
        name = {self.item:[deposit_item]}
        self.ledger.append(name)

    #buidling the withdraw method
    def withdraw(self,amount,description=""):
        withdraw_item = {"withdraw":{"amount":-amount,"description":description}}
        for item in self.ledger:
            for key,value in item.items():
                if key == self.item:
                    for _,v in value[0].items():
                        # if v["amount"] < amount:
                        if self.check_funds(amount) ==False:
                            pass
                        else:
                            value.append(withdraw_item)  
                           

    #building the get_balance method
    def get_balance(self):
        for item in self.ledger:
            for key,value in item.items():
                if key == self.item:
                    deposit_amount=value[0].get("deposit")["amount"]
                    if len(value) >1:
                        withdrawal_amoutnt = value[1].get("withdraw")["amount"]
                        deposit_amount += withdrawal_amoutnt
                    balance_amount = {"balance":{"amount":deposit_amount}}
                    value.append(balance_amount)
                    return balance_amount


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



def create_spend_chart(categories):
    pass

if __name__== "__main__":
  
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.get_balance()

    print(food.ledger)
    

