class Category:

##### Passes all tests. Still have to fix the comments and clean the code up. #####

  def __init__(self, category=None):
    self.ledger = []
    self.category = category.lower().capitalize()
    self.funds = None
    self.withdrawn = []

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
    self.withdrawn.append(withdraw_amount)
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
    self.withdrawn.append(amount)
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
    #print(stars)
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
          #print(str(v + spacing + amount))
          ledger.append((str(v + spacing + amount) + '\n'))
        if k == "balance":
          amount = (len('balance') + len(str(v)))
          spacing = (int( 30 - amount) * ' ')
          #print("balance" + spacing + str(v))
          ledger.append(("Total: " + str(v)))

    return ''.join(ledger).replace("'", '')




def create_spend_chart(categories):
  spacing = len(categories) * len(categories) + 1

  withdrawals = []
  # This if statement and for loop is to break down the list to use each category to pull out the all that was withdrawn and add it to the list withdrawals above.
  if len(categories) > 1:
    for category in categories:
      category = category.withdrawn
      withdrawals.append(category)
  else:
    category = categories.withdrawn
    withdrawals.append(category)

  # Here we are collecting the total of the amount that was witdrawn.
  totals = 0
  for withdraw in withdrawals:
    for total in withdraw:
      totals = round(float(totals + total), 2)

  # Now time to break down each specific percentage for how much each category withdrawn.
  charts = []
  for categor in categories:
    amount = 0
    amount_category = categor.withdrawn
    for amount_categ in amount_category:
      amount = round(amount_categ + amount, 2)
      amount = int((amount / totals) * 100) # This gives me percentages to 10th value.
      if amount >= 10:
        amount = round(amount, -1)
      else:
        amount = round(amount, 0)
    catty = {categor.category: amount}
    charts.append(catty)

  # This section makes breaks everything down and combines them all together to format the bar graph.
  chart_2 = ["Percentage spent by category" '\n',]
  for percent in range(0, 110, 10):   # This is going to go from 0 - 100 percent in intervals of 10 and check the categories if they are equal to the percentage.
    bars = []
    for chart in charts:
      for k, v in chart.items(): # This inserts a ' o ' if the percentage of the category is equal to the percentage or 3 spaces if not equal to the percentage.
        if percent <= v:
          bar = ' o '
        else:
          bar = 3 * ' '
        bars.append(bar)
    bars.append(' ')
    if len(str(percent)) < 3:
      if len(str(percent)) < 2:
        percent = '  ' + str(percent)
      else:
        percent = ' ' + str(percent)

    bar_chart = str(percent)+ '|' + (''.join(bars)) + '\n'
    chart_2.insert(1, bar_chart)
  chart_2.append((4 * ' ' + (spacing * '-') + '\n'))

  # Determining the longest category and putting the category into a list to make it easier to play with.
  cat_names = []
  longest = 0
  for names in categories:
    names = names.category
    cat_names.append(names)
    if longest < len(names):
      longest = len(names)

  # Formatting each Category vertically and correctly uner the corresponding bars.
  vc = []
  l = longest
  for i in range(0, longest):
    l -= 1
    vc.append(4 * ' ')
    for nam in cat_names:
      try:
        if i <= len(nam):
            vc.append(' ' + nam[i] + ' ')
      except:
        space = 3 * ' '
        vc.append(space)
      if i > len(nam):
        space = 3 * ' '
        vc.append(space)
    if l > 0:
      vc.append(' \n')
    else: 
      vc.append(' ')
  chart_2.append(''.join(vc))

  return ''.join(chart_2)
