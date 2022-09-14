class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollar, cent):
        self.dollar = dollar
        self.cent = cent 

    def add_money(self, add_dollars, add_cents):
        self.add_dollars = add_dollars
        self.add_cents = add_cents
        self.dollar += self.add_dollars
        self.cent += self.add_cents
        if self.cent > 99:
            self.dollar += self.cent // 100
            self.cent = self.cent % 100

    def show_money(self):
        print(f"total money = {self.dollar} dollar and {self.cent} cent")

my_pig = PiggyBank(0,0)
print(my_pig.dollar)

my_pig.add_money(55,40)
my_pig.show_money()


"""
class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollar, cent):
        self.dollar = dollar
        self.cent = cent 
        
    def add_money(self, add_dollars, add_cents):
        self.add_dollars = add_dollars
        self.add_cents = add_cents
        self.dollar += self.add_dollars
        self.cent += self.add_cents
        if self.cent > 99:
            self.dollar += self.cent // 100
            self.cent = self.cent % 100

"""