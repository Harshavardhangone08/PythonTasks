'''
Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance.
'''

class BankAccount:
    def __init__(self):
        self.AccountNum=123456789
        self.Balance=10000.00
        
    def deposit(self,DA):
        self.Balance+=DA
        print(f"{DA} deposited into the Account")
        print(f"Current balance:",self.Balance)
        
    def Withdraw(self,WA):
        if WA>self.Balance:
            print("Insufficient Funds!")
        else:
            self.Balance-=WA
            print(f"Transaction Successful!")
            print(f"{WA} amount debited from your Bank Account")
    def display(self):
        print("Account NUmber:",self.AccountNum)
        print("Bank Balance:",self.Balance)
        

DA=int(input("Enter ammount to be Deposited:"))
WA=int(input("Enter ammount to Withdraw:"))

BA=BankAccount()
BA.deposit(DA)
BA.Withdraw(WA)
BA.display()

