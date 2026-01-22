class BankAccount:
    
    def __init__(self,balance):
            self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    def show_balance(self):
        print(f"Balance: {self.__balance}")
        
account = BankAccount(1000)
account.show_balance()
account.deposit(500)
account.show_balance()



        
        