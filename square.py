import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	turtle.register_shape("C:\prank\poke.gif")
	brad=turtle.Turtle()
	brad.shape("C:\prank\poke.gif")
	brad.color("blue")
	brad.speed(1)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)


	window.exitonclick()





draw_square()