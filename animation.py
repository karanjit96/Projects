import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

player =turtle.Turtle()
player.shape("square")
player.color("green")

def player_animate():
    if player.shape() == "circle":
        player.shape("square")
    elif player.shape() == "square":
        player.shape("circle")
    
    #set timer
    wn.ontimer(player_animate, 500)
    
player_animate()
while True:
    wn.update()
    print("main loop")
    
    
    



wn.mainloop()