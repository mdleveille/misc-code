from turtle import *

color('green')

while True:
    speed(500)
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

done()
