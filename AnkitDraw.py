import turtle

cursor = turtle.Turtle()

def polygon(n,base): 
 extangle = 360//n
 
 for i in range(n):
  cursor.forward(base)
  cursor.right(extangle)

def circle(r):
    cursor.circle(r)

def line(length,angle):
    cursor.forward(200)
    cursor.backward(100)
    cursor.left(angle)
    cursor.forward(length)



