class BankAccount:	
    def __init__(self, tasainteres=0, balance=0):
        self.tasainteres = tasainteres
        self.balance = balance
        if self.tasainteres==0:
            self.tipo="vista"
        else:
            self.tipo="ahorro"
        print(f"Se ha creado una cuenta {self.tipo}.")
        print(f"Su saldo inicial es de ${self.balance} y su tasa de interes es de {self.tasainteres*100}%.")
        
    def __str__(self):
      return f"Tipo de cuenta: {self.tipo} - Tasa de interes: {self.tasainteres*100}% - Saldo: ${self.balance}"

    def deposit(self, monto):    
        self.balance += monto
        print(f"Se ha realizado un deposito de ${monto}.\nSu nuevo saldo es de ${self.balance}.")
        return self

    def withdraw(self, monto):
        if self.balance< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.balance}. Faltan {monto-self.balance}")
            return self
        self.balance -= monto
        print(f"Se ha realizado un giro de ${monto}.\nSu nuevo saldo es de ${self.balance}.")
        return self

    def display_account_info(self):
        print(f"Tipo de cuenta: {self.tipo} - Tasa de interes: {self.tasainteres*100}% - Saldo: ${self.balance}")
        return self

    def yield_interest(self):
        self.intereses= self.balance*self.tasainteres
        self.balance = self.balance*(1+self.tasainteres) 
        print(f"Se han cargado intereses a la cuenta por ${self.intereses}.\nSu nuevo saldo es de ${self.balance}.")
        return self  

cuentavista=BankAccount(0)
cuentaahorro=BankAccount(0.05)
cuentavista.deposit(100).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()
cuentaahorro.deposit(100).deposit(200).withdraw(10).withdraw(20).withdraw(30).withdraw(40).yield_interest().display_account_info()