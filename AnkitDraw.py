import turtle

cursor = turtle.Turtle()

def polygon(n,base): 
 extangle = 360//n
 
 for i in range(n):
  cursor.forward(base)
  cursor.right(extangle)

def circle(r):
    cursor.circle(r)

def aLine(length,angle):
    cursor.forward(200)
    cursor.backward(100)
    cursor.left(angle)
    cursor.forward(length)

def line(length,angle):
    cursor.left(angle)
    cursor.forward(length)

def rect(l,b):
 cursor.forward(l)
 cursor.left(90)
 cursor.forward(b)
 cursor.left(90)
 cursor.forward(l)
 cursor.left(90)
 cursor.forward(b)
 cursor.left(90)
 



