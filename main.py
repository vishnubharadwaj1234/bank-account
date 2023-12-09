# bank project
class Account():
  def __init__(self, name, checking, savings, pin):
    self.name = name
    self.checking = checking
    self.savings = savings
    self.pin = pin
    self.history = []
  def __repr__(self):
    return("name: " + self.name + "\nchecking: " + "${:,.2f}".format(self.checking) + "\nsavings: " + "${:,.2f}".format(self.savings) + "\nPIN: " + str(self.pin))
  def checkPin(self):
    userPin = input("Please enter your PIN. ")
    print(userPin)
    if int(userPin) == int(self.pin):
      return True
    else:
      return False
  #WITHDRAWALS
  def withdrawals(self):
    if self.checkPin():
      withdrawalAccount = input("Which account do you want to withdraw money from? ")
      if withdrawalAccount == "checking":
        withdrawalMoney = input("How much money do you mant to withdraw? ")
        if float(withdrawalMoney) <= self.checking:
          #error here. types don't match.
            self.checking -= float(withdrawalMoney)
            print("You withdrew " + "${:,.2f}".format(float(withdrawalMoney)) + " from your checking account.")
            self.history.append("WITHDRAWAL: " + "${:,.2f}".format(float(withdrawalMoney)) + " FROM CHECKING.")
        else:
          print("You don't have enough money.")
      elif withdrawalAccount == "savings":
        withdrawalMoney = input("How much money do you mant to withdraw? ")
        if float(withdrawalMoney) <= self.savings:
            self.savings -= float(withdrawalMoney)
            print("You withdrew " + "${:,.2f}".format(float(withdrawalMoney)) + " from your savings account.")
            self.history.append("WITHDRAWAL: " + "${:,.2f}".format(float(withdrawalMoney)) + " FROM SAVINGS.")
        else:
          print("You don't have enough money.")
      else:
        print("There is no account called ", withdrawalAccount, ".")
    else:
      print("Your pin is incorrect.")
  #DEPOSITS
  def deposits(self):
    if self.checkPin():
      depositsAccount = input("Which account do you want to deposit money to? ")
      if depositsAccount == "checking":
        depositsMoney = input("How much money do you want to deposit? ")
        self.checking += float(depositsMoney)
        print("You deposited " + "${:,.2f}".format(float(depositsMoney)) + " into your checking account.")
        self.history.append("DEPOSIT: " + "${:,.2f}".format(float(depositsMoney)) + " TO CHECKING.")
      elif depositsAccount == "savings":
        depositsMoney = input("How much money do you mant to deposit? ")
        self.savings += float(depositsMoney)
        print("You deposited " + "${:,.2f}".format(float(depositsMoney)) + " into your savings account.")
        self.history.append("DEPOSIT: " + "${:,.2f}".format(float(depositsMoney)) + " TO SAVINGS.")
      else:
        print("There is no account called ", depositsAccount, ".")
    else:
      print("Your pin is incorrect.")
  #DIRECTPAYMENTS
  def directPayments(self):
    if self.checkPin():
      person = input("Who are you paying? ")
      reason = input("What is the reason for the payment? ")
      dpMoney = input("How much money are you paying? ")
      dpAccount = input("Which account to you want to withdraw money from? ")
      if dpAccount == "checking":
        if float(dpMoney) <= self.checking:
          self.checking -= float(dpMoney)
          print("You payed ", person, " ${:,.2f}".format(float(dpMoney)), "from your checking account because ", reason, ".")
          self.history.append("DIRECT PAYMENT: " + "${:,.2f}".format(float(dpMoney)) + " FROM CHECKING TO " + person + ".")
        else:
          print("You don't have enough money.")
      elif dpAccount == "savings":
        if float(dpMoney) <= self.savings:
          self.savings -= float(dpMoney)
          print("You payed ", person + " ${:,.2f}".format(float(dpMoney)), "from your savings account because ", reason, ".")
          self.history.append("DIRECT PAYMENT: " + "${:,.2f}".format(float(dpMoney)) + " FROM SAVINGS TO " + person + ".")
        else:
          print("You don't have enough money.")
      else:
        print("There is no account called " + dpAccount + ".")
    else:
      print("Your pin is incorrect.")
  #TRANSFER
  def transfer(self):
    if self.checkPin():
      transferFrom = input("Which account are you transferring money from? ")
      if transferFrom == "checking":
        transferMoney = input("How much money are you transferring? ")
        if float(transferMoney) <= self.checking:
          self.checking -= float(transferMoney)
          self.savings += float(transferMoney)
          print("You transfered " + "${:,.2f}".format(float(transferMoney)) + " from checking account to savings account.")
          self.history.append("TRANSFER: " + "${:,.2f}".format(float(transferMoney)) + " FROM CHECKING TO SAVINGS.")
        else:
          print("You don't have enough money.")
      elif transferFrom == "savings":
        transferMoney = input("How much money are you transferring? ")
        if float(transferMoney) <= self.savings:
          self.savings -= float(transferMoney)
          self.checking += float(transferMoney)
          print("You transfered " + "${:,.2f}".format(float(transferMoney)) + " from savings account to checking account.")
          self.history.append("TRANSFER: " + "${:,.2f}".format(float(transferMoney)) + " FROM SAVINGS TO CHECKING.")
        else:
          print("You don't have enough money.")
      else:
        print("There is no account called " + transferFrom + ".")
    else:
      print("Your pin is incorrect.")
  #HISTORY
  def printHistory(self):
    print("Viewing transaction history for " + self.name + "'s account.")
    for entry in self.history:
      print(entry)

class ExecutiveAccount(Account):
  def __init__(self, name, checking, savings, pin):
    Account.__init__(self, name, checking, savings, pin)
    self.rewards = 0.0
    self.debt = 0.0
  def __repr__(self):
    return("name: " + self.name + "\nchecking: " + "${:,.2f}".format(self.checking) + "\nsavings: " + "${:,.2f}".format(self.savings) + "\nrewards: " + "${:,.2f}".format(self.rewards) + "\ndebt: " + "${:,.2f}".format(self.debt) + "\nPIN: " + str(self.pin))
  #EXECUTIVE DIRECTPAYMENTS
  def directPayments(self):
    if self.checkPin():
      person = input("Who are you paying? ")
      reason = input("What is the reason for the payment? ")
      dpMoney = input("How much money are you paying? ")
      dpAccount = input("Which account to you want to withdraw money from? ")
      if dpAccount == "checking":
        if float(dpMoney) <= self.checking:
          self.checking -= float(dpMoney)
          print("You payed ", person, " ${:,.2f}".format(float(dpMoney)), "from your checking account because ", reason, ".")
          self.history.append("DIRECT PAYMENT: " + "${:,.2f}".format(float(dpMoney)) + " FROM CHECKING TO " + person + ".")
          self.rewards += 0.05 * float(dpMoney)
        else:
          print("You don't have enough money.")
      elif dpAccount == "savings":
        if float(dpMoney) <= self.savings:
          self.savings -= float(dpMoney)
          print("You payed ", person + " ${:,.2f}".format(float(dpMoney)), "from your savings account because ", reason, ".")
          self.history.append("DIRECT PAYMENT: " + "${:,.2f}".format(float(dpMoney)) + " FROM SAVINGS TO " + person + ".")
          self.rewards += 0.05 * float(dpMoney)
        else:
          print("You don't have enough money.")
      else:
        print("There is no account called " + dpAccount + ".")
    else:
      print("Your pin is incorrect.")
  def loan(self):
    if self.checkPin():
      moneyNeeded = input("How much money do you need to borrow? ")
      loanAccount = input("Would you like the loan to go to checking or savings? ")
      self.debt += float(moneyNeeded)
      if loanAccount == "checking":
        self.checking += float(moneyNeeded)
        self.history.append("LOAN: " + "${:,.2f}".format(float(moneyNeeded)) + " TO CHECKING ACCOUNT.")
      elif loanAccount == "savings":
        self.savings += float(moneyNeeded)
        self.history.append("LOAN: " + "${:,.2f}".format(float(moneyNeeded)) + " TO SAVINGS ACCOUNT.")
      else:
        print("There is no account called " + loanAccount + ".")
    else:
      print("Your pin is incorrect.")
  def claimRewards(self):
    if self.checkPin():
      if self.rewards >= 25.0:
        rewardsMoney = input("How much money do want to withdraw? ")
        if float(rewardsMoney) <= self.rewards:
          rewardAccount = input("Which account do you want to deposit your rewards money in to? ")
          if rewardAccount == "checking":
            self.rewards -= float(rewardsMoney)
            self.checking += float(rewardsMoney)
            self.history.append("CLAIMED REWARDS: " + "${:,.2f}".format(float(rewardsMoney)) + " TO CHECKING ACCOUNT.")
          elif rewardAccount == "savings":
            self.rewards -= float(rewardsMoney)
            self.savings += float(rewardsMoney)
            self.history.append("CLAIMED REWARDS: " + "${:,.2f}".format(float(rewardsMoney)) + " TO SAVINGS ACCOUNT.")
          else:
            print("There is no account called " + rewardAccount + ".")
    else:
      print("Your pin is incorrect.")



# we need two accounts: checking and savings.
# the program will be menu driven that loops until exit is selected.
# we need to be able to make withdrawals, deposits, direct payments, and a transaction history.
# we need to able to transfer money between the savings and checking accounts.
# we need an exit option.
# we need to be able to print out the money the person has.

print("Welcome new user.")
print("we will proceed to account generation.")
accountLevel = input("Are you making a standard or executive account? ")
if accountLevel == "standard":
  print("You have created a standard account.")
  name = input("What is your name? ")
  pin = input("What do you want your pin to be? ")
  user = Account(name, 0.0, 0.0, pin)
  print("Welcome " + name + ".")
  while True:
    print("\nPress 1 to see your account statement.")
    print("Press 2 for a deposit.")
    print("Press 3 for withdrawals.")
    print("Press 4 for transfers.")
    print("Press 5 for payments.")
    print("Press 6 for transaction history.")
    print("Press 7 to exit.")
    choice = input("What would you like to do? \n")
    if int(choice) == 1:
      print(user)
    elif int(choice) == 2:
      user.deposits()
    elif int(choice) == 3:
      user.withdrawals()
    elif int(choice) == 4:
      user.transfer()
    elif int(choice) == 5:
      user.directPayments()
    elif int(choice) == 6:
      user.printHistory()
    elif int(choice) == 7:
      print("Thank you for using our program.")
      break
elif accountLevel == "executive":
  print("You have created an executive account.")
  name = input("What is your name? ")
  pin = input("What do you want your pin to be? ")
  user = ExecutiveAccount(name, 0.0, 0.0, pin)
  print("Welcome " + name + ".")
  while True:
    print("\nPress 1 to see your account statement.")
    print("Press 2 for a deposit.")
    print("Press 3 for withdrawals.")
    print("Press 4 for transfers.")
    print("Press 5 for payments.")
    print("Press 6 for transaction history.")
    print("Press 7 to claim rewards.")
    print("Press 8 to take a loan.")
    print("Press 9 to exit.")
    choice = input("What would you like to do? \n")
    if int(choice) == 1:
      print(user)
    elif int(choice) == 2:
      user.deposits()
    elif int(choice) == 3:
      user.withdrawals()
    elif int(choice) == 4:
      user.transfer()
    elif int(choice) == 5:
      user.directPayments()
    elif int(choice) == 6:
      user.printHistory()
    elif int(choice) == 7:
      user.claimRewards()
    elif int(choice) == 8:
      user.loan()
    elif int(choice) == 9:
      print("Thank you for using our program.")
      break