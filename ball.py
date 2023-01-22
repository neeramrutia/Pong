from turtle import Turtle
import random
class Ball(Turtle):
    randfunx=random.choice([0.2,-0.2])
    randfuny=random.choice([0.2,-0.2])
    sleeptimeofball=0
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.sleeptimeofball=0.0005
        

    def move(self):
        self.goto(self.xcor()+self.randfunx,self.ycor()+self.randfuny)

    def bounce(self):
        self.randfuny=self.randfuny*-1
        

    def bouncebypaddle(self):
        self.randfunx=self.randfunx*-1
        self.sleeptimeofball*=0.5

    def resetpos(self):
        self.goto(0,0)
        # self.write("game over",align="center")        