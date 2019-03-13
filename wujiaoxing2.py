"""
    作者：罗鹏
    功能：绘制五角星
    版本：10
    日期： 2019/02/23
"""
import turtle
import sys
from turtle import*

#changdu=50
def main():
    turtle.penup()
    turtle.backward(20)

    #turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('red')
    changdu=50
    #goto(-200,200)
    circle(30)
    while changdu <= 100:
        
        wujiaoxing(changdu)
        changdu=changdu+10
    turtle.exitonclick()

def wujiaoxing(changdu):
    i=1
    while i<=5:
        turtle.forward(changdu)
        turtle.right(144)
        i+=1




if __name__=="__main__":
    main()
