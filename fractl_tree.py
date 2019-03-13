import turtle

def draw_brach(branch_length):
    if branch_length<10:
       turtle.pencolor('green') 
    else:
        turtle.pencolor('blue') 
    if branch_length >5 :
        #右侧
        turtle.forward(branch_length)
        print("向前",branch_length)
        turtle.right(20)
        print("右转20")
        draw_brach(branch_length-15)
        #print("向后",branch_length)
        
        turtle.left(40)
        print("左转40")
        draw_brach(branch_length-15)
        #print("向前",branch_length)

        # 返回 之前的点
        turtle.right(20)
        turtle.backward(branch_length)
        #print("向后",branch_length)
        

def main():
    
    turtle.left(90)
    
    
    turtle.penup()

    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('red')
    draw_brach(100)
    turtle.exitonclick()



if __name__=="__main__":
    main()
