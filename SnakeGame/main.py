from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("LightSkyBlue2")
sc.title("Snake Game")
sc.tracer(0)

sn = Snake()
fd = Food()
scr = Score()

sc.listen()
sc.onkey(sn.up, "Up")
sc.onkey(sn.down, "Down")
sc.onkey(sn.left, "Left")
sc.onkey(sn.right, "Right")

game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.distance(fd) < 15:
        fd.refresh()
        sn.extend()
        scr.increase_score()

    if sn.head.xcor() > 290 or sn.head.xcor() < -290 or sn.head.ycor() > 290 or sn.head.ycor() <-290:
        game_on = False
        scr.game_over()

    for i in sn.segments[1:]:
        if sn.head.distance(i) < 10:
            game_on = False
            scr.game_over()


sc.exitonclick()