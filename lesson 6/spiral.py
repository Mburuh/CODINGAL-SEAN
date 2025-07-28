import turtle
t=turtle.Turtle()
s=turtle.Screen()
colors=['red','dark','green', 'blue','yellow', 'purple', 'pink','amber','violet','orange']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
        
     for x in range(300):
         
        t.pencolor(colors[x%len(colors)])
        t.forward(x)
        t.left(59)
     for x in range(300):
         t.right(239)
         t.pencolor('black')
         t.width(x/100+7)
         t.forward(x)
         t,right(59)
             