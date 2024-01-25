class Account:
    def __init__(self, owner, balance, draw, plus):
        self.owner = owner
        self.balance = balance
        self.draw = draw
        self.plus = plus

    def deposit(self):
        self.balance += self.plus
        print(self.owner)
        print("На вашем счету: " + str(self.balance) + " тенге")

    def withdraw(self):
        if self.balance < self.draw:
            print("На вашем балансе не хватает средств для снятия")
        else:
            self.balance -= self.draw
            print(self.owner)
            print("На вашем счету: " + str(self.balance) + " тенге")


name = input("Ваше имя: ")
balance = int(input("Ваш баланс: "))
user = input("Что вы хотите сделать?: ")
plus = 0  
draw = 0  

result = Account(name, balance, draw, plus)

if user == "from deposit":
    draw = int(input("Сколько хотите снять со своего счета?"))
    result.withdraw()
elif user == "into deposit":
    plus = int(input("Сколько хотите внести на свой счет?"))
    result.deposit()
elif user == "account":
    result.deposit()
