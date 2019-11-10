from turtle import Turtle
class Ball(Turtle):
	def __init__(self, radius, colour, dx, dy):
		Turtle.__init__ (self)
		Turtle.penup()
		self.radius=radius
		self.colour=colour
		self.dx=dx
		self.dy=dy
		self.shape=('circle')
		self.colour(colour)
		self.shape(r/10)
	def move(self, screen_width, screen_hight):
		self.current_x= xcor()
		self.move(x,y)
		self.new_x=xcor()
		self.current_y=ycor()
		self.move(x,y)
		self.new_y=ycor()
		right_side_ball=new_x+radius
		left_side_ball=new_x+radius
		top_side_ball=new_y+radius
		bottom_side_ball=new_y+radius
		self.goto(new+x,new_y)
		edge
		if right_side_ball



