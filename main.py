import turtle as trtl
import random as rand
#Variables
side = 0
#First size
line = 20
#door
door_size = 15
#Second side after door
wallpeice = line - door_size
#increase on each increment
wall_increase = 10
#Border
side_wall = line + door_size - wallpeice
#Bit after door
small_wall = 10
#Import Turtles
maze = trtl.Turtle()
wn = trtl.Screen()
#Main Code

def barrier():
    maze.forward(small_wall)
    maze.right(90)
    maze.forward(side_wall)
    maze.right(180)
    maze.forward(side_wall)
    maze.right(90)
def door():
    maze.penup()
    maze.forward(door_size)
    maze.pendown()
maze.goto(0,0)
maze.pensize(3)
maze.speed(0)
while side != 26:
    maze.forward(wallpeice)
    door()
    barrier()
    maze.forward(line/2)
    maze.right(90)
    line = line + wall_increase
    wallpeice = wallpeice + wall_increase
    side = side + 1

wn.mainloop()


