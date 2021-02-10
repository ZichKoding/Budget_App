class Category:
    
    def __init__(self, category=None):
        self.ledger = []
        self.category = category.lower().capitalize()
        self.funds = None

    # This method is to be able to tell you if you have enough funds with yes, "True", you have enough funds, or no, "False", you do not have enough funds.
    def check_funds(self, amount):
        if self.funds < amount:
            return False
        else:
            return True

    # Allows you to store deposit funds with the option of a description under __init__ to self.ledger in a dictionary format.
    def deposit(self, deposit_amount, deposit_descrip=None):
        self.deposit_amount = deposit_amount
        self.deposit_descrip = deposit_descrip
        self.funds = deposit_amount
        if deposit_descrip is not None:
            return self.ledger.append({"amount": self.deposit_amount, "description": deposit_descrip})
        else:
            return  self.ledger.append({"amount": self.deposit_amount, "description": ''})

    # Tells you how much you witdrew and description is optional and stores under __init__ in the self.ledger. Also, this is where it calculates the balance and stores it under __init__ in self.check_funds.
    def withdraw(self, withdraw_amount, withdraw_descrip=None):
        self.withdraw_amount = -(withdraw_amount)
        self.withdraw_descrip = withdraw_descrip
        if self.check_funds(withdraw_amount) is False:
            return False
        self.funds = self.funds - withdraw_amount
        if withdraw_descrip is not None:
            self.ledger.append({"amount": self.withdraw_amount, "description": self.withdraw_descrip})
        else:
            self.ledger.append({"amount": self.withdraw_amount, "description": ''})
        return True

    # To transfer from one objet (Category) to another and tell you where it went to and came from accordingly. It is stored inside of the ledger as if it were a withdraw if leaving and deposit if coming to.
    def transfer(self, amount, category):
        if self.check_funds(amount) is False:
            return False
        self.funds = self.funds - amount
        self.transfered = category.deposit(amount, ("Transfer from " + self.category))
        self.to_category = category.category
        self.ledger.append({"amount": -(amount), "description": ("Transfer to " + self.to_category)})
        return True


    def get_balance(self):
        return self.funds

    # This if for when its needed to print out all the details of the object.
    def __repr__(self):
        self.ledger.append({'balance': self.funds})
        ledger = []

        #Formats the title category with 30 characters long including the category in the center and the empty spaces are filled with *'s.
        c = self.category
        stars = (int((30 - len(c))/2) * ("*")) + c + (int((30 - len(c))/2) * "*")
        ledger.append((stars + '\n'))

        # Breaks the list down to the dictionaries inside the list.
        for l in self.ledger:
            # Breaks down the dictionaires and creates the correct formatting with description aligned to the left and amount aligned to the right.
            for k, v in l.items():
                if k == "description":
                    amount = l["amount"]
                    amount = str(f'{amount:.2f}')
                    spacing = (int((30 - len(v) - len(amount))) * ' ')
                    if v == []:
                        spacing = (int((30 - len(v) - len(amount) - 2)) * ' ')
                        v = str(v)
                    if len(v) >= int(30 - len(amount)):
                        v = v[0 : int(30- len(amount) -1)] + ' '
                    ledger.append((str(v + spacing + amount) + '\n'))
                if k == "balance":
                    amount = (len('balance') + len(str(v)))
                    spacing = (int( 30 - amount) * ' ')
                    ledger.append(("Total: " + str(v)))

        return ''.join(ledger).replace("'", '')


def create_spend_chart(categories):
    pass
