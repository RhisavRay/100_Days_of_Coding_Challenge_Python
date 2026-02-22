# import turtle
#
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrange")
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = "l"
print(table.align)
print(table)