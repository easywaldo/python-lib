import turtle as t

t.home()
t.shape("turtle")
t.forward(100)
t.left(120)

t.clear()
t.home()
t.shape("turtle")

import random
color_list = ["red", "green", "blue", "yellow"]
for i in range(300):
    t.forward(100)
    t.left(120)
    t.right(120)
    t.left(120)
    t.back(100)
    t.circle(120)
    pick_color = random.randrange(0, 4)
    
    t.bgcolor(color_list[pick_color])