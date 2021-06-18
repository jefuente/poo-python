class BankAccount:	
    def __init__(self, tasainteres=0.02, balance=0):
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
        return self

    def withdraw(self, monto):
        if self.balance< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.balance}. Faltan {monto-self.balance}")
            return self
        self.balance -= monto
        return self

    def display_account_info(self):
        print(f"Tipo de cuenta: {self.tipo} - Tasa de interes: {self.tasainteres*100}% - Saldo: ${self.balance}")
        return self

    def yield_interest(self):
        self.intereses= self.balance*self.tasainteres
        self.balance = self.balance*(1+self.tasainteres) 
        #print(f"Se han cargado intereses a la cuenta por ${self.intereses}.\nSu nuevo saldo es de ${self.balance}.")
        return self  

class Usuario:		# declara una clase y dale el nombre User
    def __init__(self, nombre, email,tasainteres=0.02, balance=0):
        self.nombre = nombre
        self.email = email
        self.account = BankAccount(tasainteres, balance)
        print(f"Pertenece al usuario {self.nombre}.")
                
    def __str__(self):
      return f"{self.nombre}"

    def make_deposit(self,monto):    
        self.account.deposit(monto)
        print(f"El usuario {self.nombre} ha hecho un deposito de ${monto}.\n Su nuevo saldo es de ${self.account.balance}.")
        return self

    def make_withdrawal(self, monto):#haz que este método disminuya el saldo del usuario en la cantidad especificada
        if self.account.balance< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.account.balance}. Faltan {monto-self.account.balance}")
            return self
        self.account.withdraw(monto)
        print(f"El usuario {self.nombre} ha hecho un giro de ${monto}.\n Su nuevo saldo es de ${self.account.balance}.")
        return self

    def display_user_balance(self):#haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
        print(f"Usuario {self.nombre}, saldo: ${self.account.balance}")
        return self

    def transfer_money(self, usuarioDestino, monto):
        if self.account.balance< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.account.balance}. Faltan {monto-self.account.balance}")
            return self
        usuarioDestino.account.deposit(monto)    
        self.account.withdraw(monto)
        print(f"Se ha hecho una transferencia de ${monto} desde {self.nombre} hacia {usuarioDestino.nombre}.")
        print(f"Usuario: {self.nombre}, saldo: ${self.account.balance}")
        print(f"Usuario: {usuarioDestino.nombre}, saldo: ${usuarioDestino.account.balance}")
        return self

guido = Usuario("Guido", "guido@python.com", 0.1, 1000)
monty = Usuario("Monty", "monty@python.com", 0.05, 2000)
michael = Usuario("Michael", "chino@gmail.com", 0, 3000)

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(400)

monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawal(300)
monty.make_withdrawal(400)

michael.make_deposit(100)
michael.make_withdrawal(200)
michael.make_withdrawal(300)
michael.make_withdrawal(400)

guido.transfer_money(michael,500)


