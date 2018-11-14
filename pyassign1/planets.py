import turtle
import math

Sun=turtle.Turtle()
Me=turtle.Turtle() #水星 Mercury
V=turtle.Turtle() #金星 Venus
E=turtle.Turtle() #地球 Earth
Ma=turtle.Turtle() #火星 Mars
J=turtle.Turtle() #木星 Jupiter
S=turtle.Turtle() #土星 Saturn

Sun.color('red')
Me.color('light blue')
V.color('gold')
E.color('blue')
Ma.color('red')
J.color('orange')
S.color('brown') #设置颜色

Sun.shape('circle')
Me.shape('circle')
V.shape('circle')
E.shape('circle')
Ma.shape('circle')
J.shape('circle')
S.shape('circle') #设置形状

Me.pu()
V.pu()
E.pu()
Ma.pu()
J.pu()
S.pu()

Me.setx(38.7)
V.setx(72.3)
E.setx(100)
Ma.setx(150)
J.setx(260)
S.setx(479)

Me.pd()
V.pd()
E.pd()
Ma.pd()
J.pd()
S.pd()

for x in range(359999999):
    Me.goto((30.7278/(1-0.206*math.cos(math.radians(0.96*x))))*math.cos(math.radians(0.96*x)),(30.7278/(1-0.206*math.cos(math.radians(0.96*x))))*math.sin(math.radians(0.96*x)))
    V.goto((71.7939/(1-0.007*math.cos(math.radians(0.7*x))))*math.cos(math.radians(0.7*x)),(71.7939/(1-0.007*math.cos(math.radians(0.7*x))))*math.sin(math.radians(0.7*x)))
    E.goto((98.33/(1-0.0167*math.cos(math.radians(0.6*x))))*math.cos(math.radians(0.6*x)),(98.33/(1-0.0167*math.cos(math.radians(0.6*x))))*math.sin(math.radians(0.6*x)))
    Ma.goto((136/(1-0.0934*math.cos(math.radians(0.48*x))))*math.cos(math.radians(0.48*x)),(136/(1-0.0934*math.cos(math.radians(0.48*x))))*math.sin(math.radians(0.48*x)))
    J.goto((247.286/(1-0.0489*math.cos(math.radians(0.26*x))))*math.cos(math.radians(0.26*x)),(247.286/(1-0.0489*math.cos(math.radians(0.26*x))))*math.sin(math.radians(0.26*x)))
    S.goto((451.9365/(1-0.0565*math.cos(math.radians(0.2*x))))*math.cos(math.radians(0.2*x)),(451.9365/(1-0.0565*math.cos(math.radians(0.2*x))))*math.sin(math.radians(0.2*x)))

turtle.mainloop()
