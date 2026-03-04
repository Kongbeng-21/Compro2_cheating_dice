import tkinter as tk

x_speed = 3
y_speed = 4
BALL_SIZE = 40
CANVAS_W = 400
CANVAS_H = 300

def animate():
    global x_speed, y_speed

    for ball in balls:
        canvas.move(ball, x_speed, y_speed)

        pos = canvas.coords(ball)

        if pos[0] <= 0 or pos[2] >= CANVAS_W:
            x_speed = -x_speed
        if pos[1] <= 0 or pos[3] >= CANVAS_H:
            y_speed = -y_speed

    root.after(8, animate)

root = tk.Tk()

canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack()

balls = []

for i in range(5):
    ball = canvas.create_oval(
        50*i, 50*i,
        50*i + BALL_SIZE,
        50*i + BALL_SIZE,
        fill="orange"
    )
    balls.append(ball)

animate()

root.mainloop()