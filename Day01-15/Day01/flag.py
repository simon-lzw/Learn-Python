"""
用Python的turtle模块绘制国旗
"""
import turtle

def draw_rectangle(x, y, width):
    """绘制矩形"""
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

