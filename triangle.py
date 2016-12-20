

import turtle




tom=turtle.Turtle()
tom.shape("turtle")
tom.color("green")

def create_background():
	window = turtle.Screen()
	window.bgcolor("red")

	recursive_triangle(100,4)

	window.exitonclick()

	



def recursive_triangle(side,recursion):
	if recursion==1:
		tom.begin_fill()
		for i in range(0,3):
			tom.forward(side)
			tom.left(120)
		tom.end_fill()
	else:
		# first triangle
		recursive_triangle(side/2,recursion-1)
		tom.forward(side/2)
#second triangle
		recursive_triangle(side/2,recursion-1)
		tom.backward(side/2)
		tom.left(60)
		tom.forward(side/2)
		tom.right(60)
#third triangle
		recursive_triangle(side/2,recursion-1)
		tom.left(60)
		tom.backward(side/2)
		tom.right(60)



	


create_background()