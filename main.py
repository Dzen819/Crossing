import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car = CarManager()

screen.onkey(player.move, "Up")
game_is_on = True
num = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if num == 0:
        car.create_car()
        num = 6
    car.move()
    num -= 1
    if player.ycor() >= 300:
        score.level_up()
        car.speed_up()
        player.to_start()
    for c in car.cars:
        if c.distance(player) < 30:
            score.game_over()
            game_is_on = False

screen.exitonclick()
