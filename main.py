from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.title("Pong")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

leftpaddle=Paddle((-350,0))
rightpaddle=Paddle((350,0))
ball=Ball()
score=Score()
 

screen.listen()
screen.onkey(rightpaddle.go_up,"Up")
screen.onkey(rightpaddle.go_down,"Down")
screen.onkey(leftpaddle.go_up,"w")
screen.onkey(leftpaddle.go_down,"s")

gameison=True

while gameison:
    
    time.sleep(ball.sleeptimeofball)
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()

    if ball.xcor()>330 and ball.distance(rightpaddle)<50 or ball.distance(leftpaddle)<50 and ball.xcor()<-330:
        ball.bouncebypaddle()   

    if ball.xcor()>380:
        ball.resetpos()
        score.lscore+=1
        ball.sleeptimeofball=0.0005
        score.printscore()
    if ball.xcor()<-380:
        ball.resetpos() 
        score.rscore+=1
        score.printscore()
        ball.sleeptimeofball=0.0005

      
            

screen.exitonclick()