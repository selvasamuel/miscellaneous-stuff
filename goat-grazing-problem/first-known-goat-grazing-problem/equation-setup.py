# I ran this program in an online Python sandbox. The one I used is available at
# https://www.pythonsandbox.com/turtle. The reason I did is that the turtle module
# needs the tkinter module to be installed and I couldn't get tkinter installed
# in macOS. All the material I found on the web suggested installing tkinter via
# HomeBrew but I didn't want to install HomeBrew.

import math
import turtle

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.forward(250)
t.left(180)
t.forward(500)
t.right(180)
t.forward(250)
t.left(90)
t.forward(250)
t.right(180)
t.forward(500)
t.left(180)
t.forward(250)
t.right(90)

radius = 50
angle = 45
t.circle(radius, 360)

t.left(90)
t.forward(radius)
t.right(180 - angle)
t.forward(radius)

new_radius = 15
t.left(180)
t.forward(radius - new_radius)
t.left(90)
t.circle(-new_radius, angle)

t.left(90)
t.forward(radius - new_radius)
t.left(90)
t.circle(radius, angle)
t.forward(2*math.pi*radius - angle * math.pi * radius / 180)
