
def pythonLogo():
    import turtle

    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.speed(5)
    t.pensize(2)
    t.pencolor("white")



    def s_curve():
        for i in range(90):
            t.left(1)
            t.forward(1)

    def r_curve():
        for i in range(90):
            t.right(1)
            t.forward(1)

    def l_curve():
        s_curve()
        t.forward(80)
        s_curve()

    def l_curve1():
        s_curve()
        t.forward(90)
        s_curve()

        

    def half():
        t.forward(50)
        s_curve()
        t.forward(90)
        l_curve()
        t.forward(40)
        t.left(90)
        t.forward(80)
        t.right(90)
        t.forward(10) 
        t.right(90)
        t.forward(120) #on test
        l_curve1()
        t.forward(30)
        t.left(90)
        t.forward(50)
        r_curve()
        t.forward(40)
        t.end_fill()

    def get_pos():
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.pendown()
        
    def eye():
        t.penup()
        t.right(90)
        t.forward(160)
        t.left(90)
        t.forward(70)
        t.pencolor("black")
        t.dot(35)

    def sec_dot():
        t.left(90)
        t.penup()
        t.forward(310)
        t.left(90)
        t.forward(120)
        t.pendown()

        t.dot(35)




    t.fillcolor("#306998")
    t.begin_fill()
    half()
    t.end_fill()
    get_pos()
    t.fillcolor("#FFD43B")
    t.begin_fill()
    half()
    t.end_fill()

    eye()
    sec_dot()



    def pause():
        t.speed(5)
        for i in range(100):
            t.left(90)
    pause()
    t.clear()

def batmanLogo():
    import turtle

    #initialize method
    bat = turtle.Turtle()

    #size of pointer and pen
    bat.turtlesize(1, 1, 1)
    bat.pensize(3)

    #screen info
    wn = turtle.Screen()
    wn.bgcolor("dark blue")
    wn.title("BATMAN")

    #colour
    bat.color("yellow", "black")


    #begin filling color
    bat.begin_fill()

    #turn1
    bat.left(90)   # turn pointer direction to left of 90'
    bat.circle(50, 85) #draw circle of radius = 50 and 85'
    bat.circle(15, 110)
    bat.right(180) 

    #turn 2
    bat.circle(30, 150)
    bat.right(5)
    bat.forward(10) #draw forward line of 10 units

    #turn 3
    bat.right(90)
    bat.circle(-70, 140)
    bat.forward(40)
    bat.right(110)

    #turn 4
    bat.circle(100, 30)
    bat.circle(30, 100)
    bat.left(50)
    bat.forward(50)
    bat.right(145)

    #turn5
    bat.forward(30)
    bat.left(55)
    bat.forward(10)

    #reverse

    #turn 5
    bat.forward(10)
    bat.left(55)
    bat.forward(30)

    #turn 4

    bat.right(145)
    bat.forward(50)
    bat.left(50)
    bat.circle(30, 100)
    bat.circle(100, 30)

    #turn 3
    bat.right(90)
    bat.right(20)
    bat.forward(40)
    bat.circle(-70, 140)

    #turn 2
    bat.right(90)
    bat.forward(10)
    bat.right(5)
    bat.circle(30, 150)

    #turn 1
    bat.left(180)
    bat.circle(15, 110)
    bat.circle(50, 85)

    #end color filling
    bat.end_fill()



    #end the turtle method
    #turtle.done()
    def pause():
        bat.speed(5)
        for i in range(100):
            bat.left(90)
    pause()
    bat.clear()
def driveLogo():
    import turtle
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Google Drive")
    #import turtle as t
    #bluebox
    t.begin_fill()
    t.fillcolor("blue")
    t.speed(1)
    t.forward(170)
    t.left(60)
    t.forward(50)
    #blue line
    t.left(120)
    t.forward(220)
    t.left(120)
    t.forward(50)
    t.end_fill()
    #greenbox
    t.begin_fill()
    t.fillcolor("green")
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(50)
    t.left(60)
    t.forward(150)
    t.left(60)
    t.forward(50)
    t.end_fill()

    t.pen()
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(50)
    t.penup()

    #yellow box
    t.begin_fill()
    t.fillcolor("yellow")
    t.left(125)
    t.forward(160)
    t.left(55)
    t.forward(53)
    t.left(126)
    t.forward(163)
    t.end_fill()
    #t.done()
    def pause():
        t.speed(5)
        for i in range(100):
            t.left(90)
    pause()
    t.clear()

def microsoftLogo():
    import turtle
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title("Microsoft Logo")
    s.bgcolor("black")
    s.colormode(255)
    def square():
        for i in range(4):
             t.forward(200)
             t.right(90)
            
    t.left(90)
    #yellow box  
    t.penup()
    t.goto(100,-150)
    t.pendown()
    t.color(255,187,0)
    t.begin_fill()
    square()
    t.end_fill()

    #green box         
    #turtle.left(90) 
    t.penup()
    t.goto(100,70)
    t.pendown()
    t.color(124,187,0)
    t.begin_fill()
    square()
    t.end_fill()

    #red box         
    #turtle.left(90) 
    t.penup()
    t.goto(-115,70)
    t.pendown()
    t.color(246,83,20)
    t.begin_fill()
    square()
    t.end_fill()

    #blue box         
    #turtle.left(90) 
    t.penup()
    t.goto(-115,-150)
    t.pendown()
    t.color(0,161,241)
    t.begin_fill()
    square()
    t.end_fill()
    #t.done()

    def pause():
        t.speed(5)
        for i in range(100):
            t.left(90)
    pause()
    t.clear()
def windowLogo():
    import turtle
    t=turtle.Turtle()
    s=turtle.Screen()
    s.bgcolor("black")
    s.title("Windows Logo")
    def smsquare(length,angle):
        t.forward(length)
        t.right(angle)


    t.color("deepskyblue")
    t.left(6)
    t.begin_fill()
    t.fillcolor("deepskyblue")
    smsquare(200,96)
    smsquare(150,96)
    smsquare(200,83)
    smsquare(109,85)
    t.end_fill()
    t.color("black")
    smsquare(100,96)
    smsquare(67,90)
    smsquare(100,180)
    smsquare(200,180)
    smsquare(100,270)
    t.forward(140)
    
    def pause():
        t.speed(5)
        for i in range(100):
            t.left(90)
    pause()
    t.clear()
    #turtle.exitonclick()
def google():   
    import turtle as t
    t.color('#4285F4','#4285F4') ## RBG value of color
    t.pensize(5)
    t.speed(3)

    t.forward(120)
    t.right(90)
    t.circle(-150,50)  ## first circle for red color
    t.color('#0F9D58')
    t.circle(-150,100)
    t.color('#F4B400')
    t.circle(-150,60)
    t.color('#DB4437','#DB4437')

    t.begin_fill()
    t.circle(-150,100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.circle(100,100)
    t.right(90)
    t.forward(50)
    t.end_fill()

    t.begin_fill()

    ## second circle for yellow color

    t.color("#F4B400","#F4B400")
    t.right(180)
    t.forward(50)
    t.right(90)

    t.circle(100,60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.circle(-150,60)
    t.end_fill()


    # third circle of green color
    t.right(90)
    t.forward(50)
    t.right(90)
    t.circle(100,60)
    t.color('#0F9D58','#0F9D58')
    t.begin_fill()
    t.circle(100,100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.circle(-150,100)
    t.right(90)
    t.forward(50)
    t.end_fill()


    ##Draw last circle

    t.right(90)
    t.circle(100,100)
    t.color('#4285F4','#4285F4')
    t.begin_fill()
    t.circle(100,25)
    t.left(115)
    t.forward(65)
    t.right(90)
    t.forward(42)
    t.right(90)
    t.forward(124)
    t.right(90)
    t.circle(-150,50)
    t.right(90)
    t.forward(50)

    t.end_fill()
    t.penup()
    ##FOr display the string statement(name)
    t.goto(60, -180)


    t.color("red")


    t.hideturtle()


    t.done()

    def pause():
        t.speed(5)
        for i in range(100):
            t.left(90)
        pause()
        t.clear()
                   
while True:
    print("Select Any Logo to Design")
    print("1. Python 2. Batman 3. GoogleDrive 4. Microsoft 5. Windows  6. Google")
    option = int(input("Enter option -- "))
    if option==1:
        pythonLogo()

    elif option==2:
        batmanLogo()

    elif option==3:
        driveLogo()

    elif option==4:
        microsoftLogo()

    elif option==5:
        windowLogo()

    elif option==6:
        google()
            

    else:
        print("Invalid option")
        

