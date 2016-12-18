import turtle

	

tom=turtle.Turtle()
tom.shape("turtle")
tom.color("green")

def create_background():
	window = turtle.Screen()
	window.bgcolor("red")

	draw_triangle()
	window.exitonclick()



def draw_triangle():

	tom.setx(0)
	tom.sety(0)
	coordinate()
	tom.setheading(0)
	tom.penup()

	#tom.reset()
	tom.pendown()
	tom.goto(100,0)
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.pendown()
	tom.setx(200)
	tom.sety(0)
	coordinate()
	tom.setheading(0)
	tom.penup()
	
	tom.pendown()
	tom.setx(300)
	tom.sety(0)
	coordinate()
	tom.setheading(0)
	tom.penup()
	

	tom.setx(50)
	tom.sety(100)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.setx(50)
	tom.sety(100)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.setx(250)
	tom.sety(100)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.setx(100)
	tom.sety(200)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.setx(200)
	tom.sety(200)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()

	tom.setx(150)
	tom.sety(300)
	tom.pendown()
	coordinate()
	tom.setheading(0)
	tom.penup()


	

	


def coordinate():
	tom.right(0)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	
	#tom.fillcolor("violet")

	tom.right(240)
	tom.forward(50)

	tom.left(120)
	tom.forward(50)
	tom.right(120)
	tom.forward(50)
	tom.left(240)
	tom.forward(50)



	



create_background()