# our class Ship
class Ship:
    destination = str(input())
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)

bp_capacity = 800
black_pearl = Ship("Black Pearl", bp_capacity)
print(black_pearl.sail())
