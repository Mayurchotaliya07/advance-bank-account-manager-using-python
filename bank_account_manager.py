class BankAccount:
    total_accounts = 0

    def __init__(self, account_no, balance, account_type):
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if self.account_type == "saving" and value < 1000:
            raise ValueError("Minimum balance in saving account is 1000")
        elif self.account_type == "checking" and value < 0:
            raise ValueError("Minimum balance in checking account is 0")
        self._balance = value

    @property
    def account_type(self):
        return self._account_type
    
    @account_type.setter
    def account_type(self, value):
        if hasattr(self,"_account_type"):
            raise ValueError("once you set it up, you can't change your account type")
        
        if value.lower() in ['saving', "checking"]:
            self._account_type = value.lower()
        else:
            raise ValueError("enter saving or checking only =")
            
    @classmethod
    def show_total(cls):
        print(f"Total {cls.total_accounts} accounts are created")

    @staticmethod
    def interest_rate(account_type):
        if account_type.lower() == "saving":
            print('Interest for saving account is 10% p.a')
        elif account_type.lower() == "checking":
            print('Interest for checking is 0% p.a')

    def deposit(self, value):
        if value <= 0:
            raise ValueError("You can't deposite 0 or any amount in minus")
        self._balance += value
        print("you deposited your amount succesfully")

    def withdraw(self,value):
        if value <= 0:
            raise ValueError("You can't withdraw 0 or any amount in minus")
        
        if self.account_type == "saving" and self._balance-value < 1000:
            raise ValueError("Minimum balance is 1000 you can't withdraw now")
        
        if self.account_type == "checking" and self._balance - value <0:
            raise ValueError("can't withdraw more than available balance")

        self._balance -= value
        print("You withdraw your amount succesfully")

    def apply_interest(self):
        if self.account_type == "saving":
            self.balance += self.balance * 0.10
        

# Create accounts
print("\n--- Creating Accounts ---")
try:
    acc1 = BankAccount(101, 5000, "saving")   # valid saving account
    acc2 = BankAccount(102, 2000, "checking") # valid checking account
    acc3 = BankAccount(103, 500, "saving")    # should raise ValueError (balance < 1000)
except ValueError as e:
    print("Error:", e)

# Show total accounts
BankAccount.show_total()

# Test deposit
print("\n--- Testing Deposit ---")
try:
    acc1.deposit(1000)    # valid deposit
    print("New balance acc1:", acc1.balance)
    acc2.deposit(-500)    # invalid deposit
except ValueError as e:
    print("Error:", e)

# Test withdraw
print("\n--- Testing Withdraw ---")
try:
    acc1.withdraw(2000)   # valid withdraw
    print("New balance acc1:", acc1.balance)
    acc1.withdraw(5000)   # should raise error (below 1000 min balance)
except ValueError as e:
    print("Error:", e)

try:
    acc2.withdraw(2500)   # should raise error (checking overdraft)
except ValueError as e:
    print("Error:", e)

# Test apply_interest
print("\n--- Testing Interest ---")
print("Balance before interest acc1:", acc1.balance)
acc1.apply_interest()     # saving account interest
print("Balance after interest acc1:", acc1.balance)

acc2.apply_interest()     # checking account interest
print("Balance after interest acc2:", acc2.balance)

# Test changing account type
print("\n--- Testing Account Type Change ---")
try:
    acc1.account_type = "checking"   # should raise error
except ValueError as e:
    print("Error:", e)

# Test interest rate static method
print("\n--- Static Method Interest Rate ---")
BankAccount.interest_rate("saving")
BankAccount.interest_rate("checking")

# Test creating a new account with invalid account type
print("\n--- Invalid Account Type ---")
try:
    acc4 = BankAccount(104, 2000, "current")  # should raise error
except ValueError as e:
    print("Error:", e)

    
