class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.owner)
        print(f"На вашем счету {self.balance} тенге")

    def withdraw(self, draw):
        if self.balance < draw:
            print("На вашем балансе не хватает средств для снятия")
        else:
            self.balance -= draw
            print(f"{self.owner}, на вашем счету {self.balance} тенге")


name = input("Ваше имя: ")
balance = int(input("Ваш баланс: "))
user = input("Что вы хотите сделать?(from deposit/into deposit): ")
plus = 0
draw = 0

result = Account(name, balance)

if user == "from deposit":
    draw = int(input("Сколько хотите снять со своего счета?: "))
    result.withdraw(draw)
elif user == "into deposit":
    plus = int(input("Сколько хотите внести на свой счет?: "))
    result.deposit(plus)
elif user == "account":
    result.deposit()
