from turtle import Turtle,Screen
import random
import turtle
turtle.colormode(255)

s1 = Screen()
height_scr = 400
width_Scr = 400
no_of_turtles=0
turtle_list = []
colors_list = ["red","green","pink","yellow","black","brown","orange","violet","aquamarine1","grey"]
def no_of_turtles():
    while(True):
       no_of_turtle = int(input("How many turtles you want to race? (2-10): "))
       if(2<=no_of_turtle<=10):
           return no_of_turtle
       else:
           print("Invalid no.of turtles.......Try Again")
           
# ------------------------------------------------------------------------------------------------------------------------    

def create_turtles(no_of_turtles):
    # s1= Screen()  #by default screen size is 400,300..........we have to set 400,400
    s1.setup(400,400)
    x_spacing = width_Scr//(no_of_turtles+1)
    
    for  i in range(1,no_of_turtles+1):
          new_turtle = Turtle()
          new_turtle.color(colors_list[i])
          new_turtle.shape("turtle")
          new_turtle.left(90)
          new_turtle.penup()
          new_turtle.goto(-width_Scr//2+(i*x_spacing), -height_scr//2+10)
          turtle_list.append(new_turtle)
   
# ------------------------------------------------------------------------------------------------------------

def  race():
    is_race_on = True
    while is_race_on:
      for  t in turtle_list:
        distance = random.randrange(1,20)
        t.forward(distance)
        x,y = t.pos()
        if(y>=height_scr//2):
            print(f"The winner is {t.fillcolor()} turtle.")
            is_race_on=False
        




no_of_turtles = no_of_turtles()
create_turtles(no_of_turtles)
race()

s1.exitonclick()
