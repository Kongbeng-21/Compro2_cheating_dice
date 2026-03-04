import tkinter as tk
import random

# ======================
# Shape Base Class
# ======================
class Shape:
    def __init__(self, canvas, canvas_width, canvas_height, color, outline):

        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # random size
        self.size = random.randint(10, 30)

        # random starting position
        self.x = random.randint(0, canvas_width - self.size)
        self.y = random.randint(0, canvas_height - self.size)

        # random velocity
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

        # prevent very slow speed
        while abs(self.vx) < 0.3:
            self.vx = random.uniform(-2, 2)
        while abs(self.vy) < 0.3:
            self.vy = random.uniform(-2, 2)

        self.color = color
        self.outline = outline
        self.id = None

        # speed multiplier (controlled by slider)
        self.speed_multiplier = 1

    def move(self):

        # move object
        self.canvas.move(
            self.id,
            self.vx * self.speed_multiplier,
            self.vy * self.speed_multiplier
        )

        pos = self.canvas.coords(self.id)

        # bounce logic
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():
            self.vx = -self.vx

        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():
            self.vy = -self.vy


# ======================
# Ball Class
# ======================
class Ball(Shape):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.id = self.canvas.create_oval(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size,
            fill=self.color,
            outline=self.outline
        )


# ======================
# Rectangle Class
# ======================
class Rectangle(Shape):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.id = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size,
            fill=self.color,
            outline=self.outline
        )


# ======================
# Canvas with Animation
# ======================
class BouncingShapeCanvas(tk.Canvas):

    def __init__(self, master, width=400, height=300,
                 color="orange", outline="red",
                 num_shapes=50, **kwargs):

        super().__init__(
            master,
            width=width,
            height=height,
            bg="white",
            highlightthickness=1,
            highlightbackground="gray",
            **kwargs
        )

        self.shapes = []

        # create shapes
        for i in range(num_shapes):

            if i % 2 == 0:
                shape = Ball(self, width, height, color, outline)
            else:
                shape = Rectangle(self, width, height, color, outline)

            self.shapes.append(shape)

        self.animate()

    # animation loop
    def animate(self):

        for shape in self.shapes:
            shape.move()

        self.after(8, self.animate)

    # change speed from slider
    def set_speed(self, speed):

        for shape in self.shapes:
            shape.speed_multiplier = speed

    # change color
    def set_color(self, color):

        for shape in self.shapes:
            self.itemconfig(shape.id, fill=color)


# ======================
# Main GUI
# ======================
def main():

    root = tk.Tk()
    root.title("Bouncing Shapes Control Panel")

    # ======================
    # Layout Frames
    # ======================

    left_frame = tk.Frame(root, bg="white")
    left_frame.grid(row=0, column=0, sticky="ns", padx=10)

    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew")

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # ======================
    # Create Canvas Grid
    # ======================

    canvases = []

    c1 = BouncingShapeCanvas(right_frame,
                             color="#FF9800",
                             outline="#E65100")

    c1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    c2 = BouncingShapeCanvas(right_frame,
                             color="#2196F3",
                             outline="#1565C0")

    c2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    c3 = BouncingShapeCanvas(right_frame,
                             color="#4CAF50",
                             outline="#2E7D32")

    c3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    c4 = BouncingShapeCanvas(right_frame,
                             color="#9C27B0",
                             outline="#6A1B9A")

    c4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    canvases.extend([c1, c2, c3, c4])

    # allow resize
    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_rowconfigure(1, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=1)

    # ======================
    # Speed Control
    # ======================

    tk.Label(left_frame,
             text="Speed Control",
             bg="white",
             font=("Arial", 12, "bold")
             ).pack(pady=10)

    def update_speed(value):

        speed = float(value)

        for canvas in canvases:
            canvas.set_speed(speed)

    speed_slider = tk.Scale(
        left_frame,
        from_=-5,
        to=5,
        resolution=0.1,
        orient="horizontal",
        command=update_speed
    )

    speed_slider.set(1)
    speed_slider.pack(pady=10)

    # ======================
    # Color Control
    # ======================

    tk.Label(left_frame,
             text="Color",
             bg="white",
             font=("Arial", 12, "bold")
             ).pack(pady=10)

    color_var = tk.StringVar(value="red")

    def update_color():

        color = color_var.get()

        for canvas in canvases:
            canvas.set_color(color)

    colors = ["red", "blue", "green", "orange", "purple"]

    for c in colors:

        tk.Radiobutton(
            left_frame,
            text=c,
            value=c,
            variable=color_var,
            command=update_color,
            bg="white"
        ).pack(anchor="w")

    root.mainloop()


# ======================
# Run Program
# ======================
if __name__ == "__main__":
    main()