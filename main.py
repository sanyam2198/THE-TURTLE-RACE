                              # ------------------TURTLE RACE GAME -----------------
  
  #   Developed By : Sanyam Sood  ^-^
  #  https://repl.it/repls/DearestDigitalSpof 
  
  
from turtle import *
from random import randint
speed(100)
penup()
goto(-140,140)

for step in range (15):
  write(step,align='center')
  right(90)
  forward(10)
  pendown()
  for step2 in range(5):
    forward(15)
    penup()
    forward(15)
    pendown()
  penup()
  back(160)
  left(90)
  forward(20)


ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-170,100)
ada.right(360)
ada.pendown()

bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-170,75)
bob.right(360)
bob.pendown()

chi=Turtle()
chi.color('orange')
chi.shape('turtle')
chi.penup()
chi.goto(-170,50)
chi.right(360)
chi.pendown()

dro=Turtle()
dro.color('green')
dro.shape('turtle')
dro.penup()
dro.goto(-170,25)
dro.right(360)
dro.pendown()

for turn in range(102):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  chi.forward(randint(1,5))
  dro.forward(randint(1,5))
