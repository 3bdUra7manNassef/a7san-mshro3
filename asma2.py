
import turtle

win = turtle.Screen()
win.setup(500, 600)

colors = ['red4', 'yellow4', 'cyan4']
color_in = int(input('Choose a color: \n1 - red\n2 - yellow\n3 - blue\n'))

if color_in == 1:
    win.bgcolor(colors[0])
elif color_in == 2:
    win.bgcolor(colors[1])
elif color_in == 3:
    win.bgcolor(colors[2])
else:
    print("Invalid input")

ism_alsha5s = raw_input('sho ismak: ')

abo_grgr = turtle.Turtle()
abo_grgr.penup()
abo_grgr.goto(0, 0)
abo_grgr.pensize(5)
abo_grgr.hideturtle()
abo_grgr.write(ism_alsha5s, align="center", font=("Courier", 24, "normal"))


turtle.mainloop()
