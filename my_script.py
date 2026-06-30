# /// script
# requires-python = ">=X.XX" TODO: Update this to the minimum Python version you want to support
# dependencies = [
#   TODO: Add any dependencies your script requires
# ]
# ///

# TODO: Update the main function to your needs or remove it.


def main() -> None:
    print("Start coding in Python today!")
    # import turtle
    # import colorsys
    # t = turtle.Turtle()
    # s = turtle.Screen() . bgcolor('black')
    # t.speed(0)
    # n = 70
    # h = 0
    # for i in range (360):
    #     c = colorsys.hsv_to_rgb(h,1,0.8)
    #     h+= 1/n
    #     t.color(c)
    #     t.left(1)
    #     t.fd(1)
    #     for j in range (2):
    #         t.left(2)
    #         t.circle(200)

from turtle import *
import colorsys
speed(0)
bgcolor('black')
h = 0
for i in range (16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 2.5)

























































# if __name__ == "__main__":
    main()
