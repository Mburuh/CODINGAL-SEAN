import turtle
turtle.Screen().bgcolor('LIGHTBLUE')
sc=turtle.Screen()
sc.setup(500,600)
turtle.title('tutle world')
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1