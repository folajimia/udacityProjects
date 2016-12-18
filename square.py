import turtle

def draw_square():
	#window = turtle.Screen()
	#window.bgcolor("white")
	draw=0
	turtle.register_shape("C:\prank\poke.gif")
	brad=turtle.Turtle()
	brad.shape("C:\prank\poke.gif")
	brad.color("yellow")
	brad.speed(1)
	while draw < 4:
		brad.forward(100)
		brad.right(90)
		draw+=1

def create_background():
	window = turtle.Screen()
	window.bgcolor("red")
	draw_square()
	draw_circle()
	draw_triangle()
	window.exitonclick()

def draw_circle():
	angie=turtle.Turtle()
	angie.circle(100)
	angie.shape("arrow")
	angie.color("blue")
	angie.speed("3")

def draw_triangle():
	tom=turtle.Turtle()
	tom.shape("turtle")
	tom.color("green")

	#tom.right(45)
	#tom.forward(100)
	#tom.right(90)
	#tom.forward(100)
	#tom.right(135)
	#tom.forward(130)

	tom.left(120)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)



create_background()