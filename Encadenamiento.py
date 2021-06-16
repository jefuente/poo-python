class Usuario:		# declara una clase y dale el nombre User
    def __init__(self, nombre, email, balanceCuenta):
        self.nombre = nombre
        self.email = email
        self.balanceCuenta = balanceCuenta
        print(f"Se ha creado el usuario {self.nombre}.")
        print(f"Su saldo inicial es de ${self.balanceCuenta}.")
        
    def __str__(self):
      return f"{self.nombre}"

    def make_deposit(self,monto):    
        self.balanceCuenta += monto
        print(f"El usuario {self.nombre} ha hecho un deposito de ${monto}.\n Su nuevo saldo es de ${self.balanceCuenta}.")
        return self

    def make_withdrawal(self, monto):#haz que este método disminuya el saldo del usuario en la cantidad especificada
        if self.balanceCuenta< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.balanceCuenta}. Faltan {monto-self.balanceCuenta}")
            return self
        self.balanceCuenta -= monto
        print(f"El usuario {self.nombre} ha hecho un giro de ${monto}.\n Su nuevo saldo es de ${self.balanceCuenta}.")
        return self

    def display_user_balance(self):#haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
        print(f"Usuario {self.nombre}, saldo: ${self.balanceCuenta}")#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
        return self

    def transfer_money(self, usuarioDestino, monto):#haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
        if self.balanceCuenta< monto:
            print (f"No tiene saldo suficiente. Saldo : [{self.balanceCuenta}. Faltan {monto-self.balanceCuenta}")
            return self
        usuarioDestino.make_deposit(monto)    
        self.make_withdrawal(monto)
        print(f"Se ha hecho una transferencia de ${monto} desde {self.nombre} hacia {usuarioDestino.nombre}.")
        print(f"Usuario: {self.nombre}, saldo: ${self.balanceCuenta}")
        print(f"Usuario: {usuarioDestino.nombre}, saldo: ${usuarioDestino.balanceCuenta}")#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
        return self

guido = Usuario("Guido", "guido@python.com", 1000)
monty = Usuario("Monty", "monty@python.com", 2000)
michael = Usuario("Michael", "chino@gmail.com", 3000)

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(400)
monty.make_deposit(100).make_deposit(200).make_withdrawal(300).make_withdrawal(400)
michael.make_deposit(100).make_withdrawal(200).make_withdrawal(300).make_withdrawal(400)
guido.transfer_money(michael,500)

