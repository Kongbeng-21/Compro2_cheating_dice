import tkinter as tk
import random

BALL_SIZE = 40
CANVAS_W = 400
CANVAS_H = 300

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow"]

balls = []
velocities = []

def animate():
    for i, ball in enumerate(balls):

        vx, vy = velocities[i]

        canvas.move(ball, vx, vy)
        pos = canvas.coords(ball)

        if pos[0] <= 0 or pos[2] >= CANVAS_W:
            vx = -vx
        if pos[1] <= 0 or pos[3] >= CANVAS_H:
            vy = -vy

        velocities[i] = (vx, vy)

    root.after(8, animate)


root = tk.Tk()


canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack()


for i in range(5):

    x = random.randint(0, CANVAS_W - BALL_SIZE)
    y = random.randint(0, CANVAS_H - BALL_SIZE)

    color = random.choice(colors)

    ball = canvas.create_oval(
        x, y,
        x + BALL_SIZE,
        y + BALL_SIZE,
        fill=color
    )

    balls.append(ball)

    vx = random.randint(-5,5)
    vy = random.randint(-5,5)

    if vx == 0: vx = 3
    if vy == 0: vy = 4

    velocities.append((vx,vy))

animate()

root.mainloop()