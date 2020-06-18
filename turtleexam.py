Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t

 

def turn_right():                 
    t.setheading(0)               
    t.forward(10)
def turn_up():                    

    t.setheading(90)

    t.forward(10)

 

def turn_left():                 

    t.setheading(180)

    t.forward(10)

 

def turn_down():                  

    t.setheading(270)

    t.forward(10)

 

def blank():                      

    t.clear()

 

t.shape("turtle")                

t.speed(0)                        

t.onkey(turn_right, "Right") 

t.onkey(turn_up, "Up")

t.onkey(turn_left, "Left")

t.onkey(turn_down, "Down")

t.onkey(blank, "Escape")   

t.listen()             

SyntaxError: multiple statements found while compiling a single statement
>>> 
=== RESTART: C:/Users/student/AppData/Local/Programs/Python/Python37/sdfas.py ==
>>> 