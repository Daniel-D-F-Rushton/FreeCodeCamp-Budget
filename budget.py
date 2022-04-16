class Category:
  def __init__(self, cat):
    self.category = cat
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})
 
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, place):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {place.category}")
      place.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    if self.balance >= amount:
      return True
    return False

  def __repr__(self):
    title = self.category.center(30, "*") + "\n"
    ledger_items = ""
    for item in self.ledger:
      desc = f"{item['description']:<23}"
      itm = f"{item['amount']:>7.2f}"
      ledger_items += f"{desc[0:23]}{itm:7}\n"
    total = f"Total: {self.balance:.2f}"
    return title + ledger_items + total

  

  
  
  





def create_spend_chart(categories):
  spent_per_category = []  
  descriptions = []
  for cat in categories:
    descriptions.append(cat.category)
    spent = 0
    for item in cat.ledger:
      if item["amount"] <= 0:
        spent += item["amount"]
    spent_per_category.append(spent)

  total = sum(spent_per_category)
  one_percent = total / 100
  percentages = []
  for cat in spent_per_category:
    rounded = cat / one_percent
    rounded -= rounded % 10
    percentages.append(rounded)

  title = "Percentage spent by category\n"
  display = ""
  for percent in range(100, -1, -10):
    display += f"{percent:>3}|"
    for cat_percent in percentages:
      if cat_percent >= percent:
        display += " o "
      else:
        display += "   "
      
    display += " \n"
  dashes = "    " + ("-" * (3 * len(categories))) + "-\n"
  
  longest = len(max(descriptions, key=len))
  cat_list = ""
  for letter in range(longest):
    cat_list += "    "
    for cat in range(len(categories)):
      if len(descriptions[cat]) > letter:
        cat_list += f" {descriptions[cat][letter]} "
      else:
        cat_list += "   "
    if letter < longest - 1:
      cat_list += " \n"
    else:
      cat_list += " "

  return title + display + dashes + cat_list  