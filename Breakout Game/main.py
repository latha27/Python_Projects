from turtle import Screen
from ball import Ball
from block import Bricks
from paddle import Paddle
from score import Scoreboard
from ui import UI
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Breakout Game")
screen.bgcolor('black')
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()
bricks = Bricks()
ui = UI()
ui.header()
score = Scoreboard(lives=5)

game_paused = False
game_is_on = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkey(key='space', fun=pause_game)


while game_is_on:
    if not game_paused:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # detect collision with x_wall:
        if ball.xcor() < -350 or ball.xcor() > 350:
            ball.bounce_x()

        # detect collision with upper wall:
        if ball.ycor() > 280:
            ball.bounce_y()

        # detect collision with Bottom wall:
        # In this case, user failed to hit the ball
        # thus he loses. The game resets.
        if ball.ycor() < -280:
            ball.reset_position()

        # detect collision with paddle:
        if ball.distance(paddle) < 50 and ball.ycor() < -250:
            # If Paddle is on Right of Screen
            if paddle.xcor() > 0:
                if ball.xcor() > paddle.xcor():
                    ball.bounce_x()
                else:
                    ball.bounce_y()
            # If Paddle is on left of Screen
            elif paddle.xcor() < 0:
                if ball.xcor() > paddle.xcor():
                    ball.bounce_x()
                else:
                    ball.bounce_y()
            # Else Paddle is in the Middle horizontally
            else:
                if ball.xcor() > paddle.xcor():
                    ball.bounce_x()
                    ball.bounce_y()
                elif ball.xcor() < paddle.xcor():
                    ball.bounce_y()
                    ball.bounce_x()
                else:
                    ball.bounce_y()

        # detect collision with bricks:
        for brick in bricks.bricks:
            if ball.distance(brick) < 40:
                score.increase_score()
                brick.quantity -= 1
                if brick.quantity == 0:
                    brick.clear()
                    brick.goto(3000, 3000)
                    bricks.bricks.remove(brick)

                # detect collision from left
                if ball.xcor() < brick.left_wall:
                    ball.bounce_x()
                # detect collision from right
                elif ball.xcor() > brick.right_wall:
                    ball.bounce_x()
                # detect collision from right
                elif ball.ycor() > brick.upper_wall:
                    ball.bounce_y()
                # detect collision from right
                elif ball.ycor() > brick.bottom_wall:
                    ball.bounce_y()
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()




screen.exitonclick()

