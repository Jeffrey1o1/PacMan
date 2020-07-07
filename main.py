def main():
    #set up the screen
    import turtle
    import math
    import random
    import time
    import tkinter.messagebox

    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Pacman")
    window.setup(700,700)
    turtle.setundobuffer(1)
    turtle.fd(0)
    turtle.tracer(50)

    class Game():
        def __init__(self):
            self.score = 0
            self.state = "splash"
            self.pen = turtle.Turtle()
            self.lives = 3
        
        def show_status(self):
            self.pen.clear()
            if game.lives > 0:
                msg = "Lives: %s Score: %s " %(self.lives, self.score)
            else:
                msg = "Game Over Score: %s" %(self.score)
            self.pen.penup()
            self.pen.goto(0, 300)
            self.pen.color("white")
            self.pen.write(msg, font=("Arial", 24, "normal"))
            self.pen.hideturtle()

    game = Game()
    game.show_status()

    #pictures
    turtle.register_shape("pacman_left.gif")
    turtle.register_shape("pacman_right.gif")

    #create pen
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)

    #create player
    class  PLayer(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("pacman_right.gif")
            self.color("yellow")
            self.penup()
            self.speed(0)
    
        def move_up(self):
            if (player.xcor(),player.ycor()+24) not in walls:
                self.goto(self.xcor(),self.ycor()+24)
        def move_down(self):
            if(player.xcor(),player.ycor()-24) not in walls:
                self.goto(self.xcor(),self.ycor()-24)
        def move_left(self):
            self.shape("pacman_left.gif")
            if(player.xcor()-24,player.ycor()) not in walls:
                self.goto(self.xcor()-24,self.ycor())
        def move_right(self):
            self.shape("pacman_right.gif")
            if(player.xcor()+24,player.ycor()) not in walls:
                self.goto(self.xcor()+24,self.ycor())
        def is_touching(self,other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a**2)+(b**2))

            if distance < 5:
                return True
            else:
                return False

    class Coin(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("white")
            self.penup()
            self.shapesize(0.25,0.25)
            self.speed(0)
            self.goto(x,y)

        def delete(self):
            self.goto(2000,2000)
            self.hideturtle()

    class Enemy(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("turtle")
            self.color("red")
            self.penup()
            self.speed(0)
            self.goto(x,y)
            self.direction = random.choice(["up","down","left","right"])
        def move(self):
            if self.direction == "up":
                dx = 0
                dy = 24
            elif self.direction == "down":
                dx = 0
                dy = -24
            elif self.direction == "left":
                dx = -24
                dy = 0
            elif self.direction == "right":
                dx = 24
                dy = 0
            else:
                dx = 0
                dy = 0
            
            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction = "left"
                elif player.xcor() > self.xcor():
                    self.direction = "right"
                elif player.ycor() < self.ycor():
                    self.direction = "down"
                elif player.ycor() > self.ycor():
                    self.direction = "up"

            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            if(move_to_x,move_to_y) not in walls:
                self.goto(move_to_x,move_to_y)
            else:
                self.direction = random.choice(["up","down","left","right"])

            turtle.ontimer(self.move,t=random.randint(100,300))

        def is_close(self,other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b **2))
            if distance < 75:
                return True
            else:
                return False

    #Create levels list
    levels = [""]

    #first level
    level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxx",
    "xP CCCCCCCCCCCCCCCCCCCCx",
    "x xxxxxxxxCxxxxxCxxxxxCx",
    "xCCCCCCCCCCxCCCCCCCCCCCx",
    "xCxxxxxxxxCCCxxxCxxxxxCx",
    "xCx      xCxCCCxCx   xCx",
    "xCx      xCCCxCxCxxxxxCx",
    "xCx      xCxCxCxCCCCCxCx",
    "xCx      xCCCCCxCxCxCxCx",
    "xCxxxxxxxxCxCxxxxxCxCxCx",
    "xCxCCCCCCCCCCCCCCCCCCCCx",
    "xCxCxxCxxxxxCxxxx xxxx x",
    "xCxCCCCxCCCCCx e  xee  x",
    "xCxCxxCxCxxxCx    xee  x",
    "xCxCCCCxCxxxCxxxx xxxx x",
    "xCxCxxCxCCCCCCCCxCCCCxCx",
    "xCxCCCCxCxxxCxxCxCxxCxCx",
    "xCxCxxCxCCCCCCCCxCCCCxCx",
    "xCxCCCCxxxxxCxxxxCxxxxCx",
    "xCCCCxCCCCCCCCCCCCCCCCCx",
    "xCxxxCCCCCxxxCCCCCxxxCCx",
    "xCCCCCxxxCCCCCxxxCCCCCxx",
    "xCxxxCCCCCxxxCCCCCxxxCCx",
    "xxxxxxxxxxxxxxxxxxxxxxxx"
    ]

    #add a coin list
    coins = []

    enemies = []
    #add level to list
    levels.append(level_1)

    #create level setup
    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)
                if character == "x":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x,screen_y))
                if character == "P":
                    player.goto(screen_x,screen_y)
                if character == "C":
                    coins.append(Coin(screen_x, screen_y))
                if character == "e":
                    enemies.append(Enemy(screen_x,screen_y))

    pen = Pen()
    player = PLayer()
    walls = []
    setup_maze(levels[1])

    #keyboard movement
    turtle.listen()
    turtle.onkey(player.move_left,"a")
    turtle.onkey(player.move_right,"d")
    turtle.onkey(player.move_up,"w")
    turtle.onkey(player.move_down,"s")

    for enemy in enemies:
        turtle.ontimer(enemy.move, t=500)

    game.state = "playing"
    #Main Game Loop

    while True:
        window.update()
        
        if game.state == "restart":
            window.clear()
            main()
        
        if game.state == "playing":
            for coin in coins:
                if player.is_touching(coin):
                    game.score+=10
                    if game.score == 2500:
                        game.state = "winner"
                    window.delay(5)
                    game.show_status()
                    coin.delete()
                    coins.remove(coin)

            for enemy in enemies:
                if player.is_touching(enemy):
                    player.goto(-264,264)
                    enemies[0].goto(192,0)
                    enemies[1].goto(192,-24)
                    enemies[2].goto(168,0)
                    enemies[3].goto(168,-24)
                    enemies[4].goto(96,0)
                    game.lives -= 1
                    if game.lives < 1:
                        game.state = "gameover"
                    window.delay(5)
                    game.show_status()
        
        if game.state == "gameover":
            if tkinter.messagebox.askyesno("Game Over", "Play Again?") == True:
                game.state = "restart"
            else:
                exit()

        if game.state == "winner":
            if tkinter.messagebox.askyesno("You Win!", "Play Again?") == True:
                game.state = "restart"
            else:
                exit()




    delay = input("Press enter to finish.")

main()
