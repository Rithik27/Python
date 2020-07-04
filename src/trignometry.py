import turtle
import math

z = turtle.Pen()
z.hideturtle()
a = input("what is the length of your first side? ")
b = input("what is the length of your second side? ")
c = input("what is the length of your third side? ")
side_1 = int(a)
side_2 = int(b)
side_3 = int(c)
angle_1 = (side_1 * side_1 + side_2 * side_2 - side_3 * side_3) / (2 * side_1 * side_2)
angle_2 = (side_2 * side_2 + side_3 * side_3 - side_1 * side_1) / (2 * side_2 * side_3)
angle_3 = (side_3 * side_3 + side_1 * side_1 - side_2 * side_2) / (2 * side_3 * side_1)
z.forward(side_1)
z.left(180 - (math.degrees(math.acos(angle_1))))
z.forward(side_2)
z.left(180 - (math.degrees(math.acos(angle_2))))
z.forward(side_3)
z.left(180 - (math.degrees(math.acos(angle_3))))
