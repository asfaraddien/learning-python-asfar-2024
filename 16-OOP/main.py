# from turtle import Turtle, Screen
#
# robert = Turtle()
# robert.shape("turtle")
# robert.shapesize(13)
# robert.color("blue")
#
# window = Screen()
# window.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Nama", ["Asfar", "Bilqisth", "Taqi"])
table.add_column("Umur", [19, 18, 16])
table.align = "l"
print(table.align)
print(table)