class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))

    def convert_cargo(self):
        return self.cargo * 1000

black_pearl = Ship("Black Pearl", 800)
print(black_pearl.convert_cargo())