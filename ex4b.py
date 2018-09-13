# ex4b.py nrg
import turtle
w = turtle.Screen()
w.bgcolor("#000000")
t = turtle.Turtle()
color("#FF0000", "#00BFFF", "	#FFD700", "#00C957", "#9B30FF")

def thepoly(size):
	for i in range(69696):
		t.fd(size)
		t.left(69)
		size = size + .2
		t.speed(0)

thepoly(69)
holdit = input();
