
import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
GAME_TIME = 20
COLORS = ["red", "gold", "green", "orange", "purple", "cyan"]


#CLASS 1: one circle 

class Circle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.r = 25                                  
        self.x = 0
        self.y = 0
        self.id = canvas.create_oval(0, 0, 0, 0, fill="red")
        self.jump()                                   

# while loop: choose a new place far from the old place

    def jump(self):
        old_x, old_y = self.x, self.y
        new_x, new_y = old_x, old_y
        while abs(new_x - old_x) < 100 and abs(new_y - old_y) < 100:
            new_x = random.randint(40, WIDTH - 40)
            new_y = random.randint(80, HEIGHT - 40)
        self.x = new_x
        self.y = new_y
        self.canvas.coords(self.id, self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r)
        self.canvas.itemconfig(self.id, fill=random.choice(COLORS))

    def is_hit(self, mouse_x, mouse_y):
        distance_x = mouse_x - self.x
        distance_y = mouse_y - self.y
        return distance_x ** 2 + distance_y ** 2 <= self.r ** 2


#CLASS 2: the whole game 

class Game:
    def __init__(self, root):
        self.root = root
        root.title("Click the Circle")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)   # left mouse click

        self.score = 0
        self.time_left = GAME_TIME
        self.playing = True

# text at the top of the screen

        self.info = self.canvas.create_text(
            10, 20, anchor="w", fill="white", font=("Arial", 14, "bold"),
            text="Score: 0    Time: " + str(GAME_TIME))

 # for loop: make 3 circles

        self.circles = []
        for i in range(3):
            self.circles.append(Circle(self.canvas))

        self.countdown()

    def on_click(self, event):
        if not self.playing:
            return

# for loop: check every circle

        for c in self.circles:
            if c.is_hit(event.x, event.y):
                self.score += 1
                c.jump()
                break
        self.show_info()

    def show_info(self):
        self.canvas.itemconfig(
            self.info,
            text="Score: " + str(self.score) + "    Time: " + str(self.time_left))

    def countdown(self):
        self.show_info()
        if self.time_left == 0:
            self.game_over()
        else:
            self.time_left -= 1
            self.root.after(1000, self.countdown)      # run again after 1 second

    def game_over(self):
        self.playing = False
        self.canvas.create_text(
            WIDTH / 2, HEIGHT / 2, fill="white", font=("Arial", 28, "bold"),
            text="TIME UP!\nScore: " + str(self.score))


#START THE GAME

root = tk.Tk()
Game(root)
root.mainloop()