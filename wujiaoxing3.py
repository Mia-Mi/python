"""
    作者：罗鹏
    功能：绘制五角星
    版本：10
    日期： 2019/02/23
"""
import turtle
import sys
from turtle import*


def main():
    wujiaoxing(50)
    turtle.exitonclick()


def wujiaoxing(chengdu):
    i=1
    while i <=5 :
            turtle.forward(chengdu)
            turtle.right(144)
            i+=1
        #print("changdu1",changdu)
    chengdu+=10
    if chengdu <= 200:
        wujiaoxing(chengdu)

if __name__=="__main__":
    main()
