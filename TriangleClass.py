class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = (self.a * self.b) / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]


# write your code here
if pow(input_c, 2) == pow(input_a, 2) + pow(input_b, 2):
    your_triangle = RightTriangle(input_c, input_a, input_b)
    print(your_triangle.area)

else:
    print("Not right")
