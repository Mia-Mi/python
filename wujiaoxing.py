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
    #turtle.forward(100)
    #turtle.backward(20)
    #turtle.right(30)
    #pencolor(255,155,192)#画笔颜色
    #color(160,82,45)
    #circle(5)
    '''
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    '''
    wujiaoxing(5)


    
    turtle.exitonclick()


def wujiaoxing(chengdu):
    i=1
    
    while(int(chengdu)<20):
        
        for num in range(0,5):
            turtle.forward(10*chengdu)
            turtle.right(144)
        #print("changdu1",changdu)
    
        wujiaoxing(chengdu+1)
        i+=1
        print("iiiiii",i)
        if int(i)>2:
            print("dayu2",(int(i)>2))
            #break
            #sys.exit()
            turtle.exitonclick()
        #return chengdu



if __name__=="__main__":
    main()
