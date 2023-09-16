# GlowScript 1.1 VPython

g = graph(width=460, height=460, ymin=-7, ymax=7, xmin=-7, xmax=7)
c1 = gcurve(color=color.red)
c2 = gcurve(color=color.blue)
c3 = gcurve(color=color.purple)

t = 0
dt = 0.01

while t <= 2*pi:
  x = (2*pi - t)*cos(t) + sin(t)
  y = (2*pi - t)*sin(t) + (1 - cos(t))
  c1.plot(x, y)
  c2.plot(-x, y)

  t = t + dt

t = 0
while t <= pi:
  x = 2 * pi * cos(t)
  y = -2 * pi * sin(t)
  c3.plot(x, y)
  
  t = t + dt
