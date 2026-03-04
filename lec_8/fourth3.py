import tkinter as tk
import random

# ==============================
# Shape Base Class
# ==============================
class Shape:

    def __init__(self, canvas, canvas_width, canvas_height, color, outline):

        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.size = random.randint(10,30)

        self.x = random.randint(0, canvas_width-self.size)
        self.y = random.randint(0, canvas_height-self.size)

        self.vx = random.uniform(-2,2)
        self.vy = random.uniform(-2,2)

        while abs(self.vx) < 0.3:
            self.vx = random.uniform(-2,2)

        while abs(self.vy) < 0.3:
            self.vy = random.uniform(-2,2)

        self.color = color
        self.outline = outline
        self.id = None

        self.speed_multiplier = 1


    def move(self):

        self.canvas.move(
            self.id,
            self.vx * self.speed_multiplier,
            self.vy * self.speed_multiplier
        )

        pos = self.canvas.coords(self.id)

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if pos[0] <= 0 or pos[2] >= width:
            self.vx = -self.vx

        if pos[1] <= 0 or pos[3] >= height:
            self.vy = -self.vy


# ==============================
# Ball Class
# ==============================
class Ball(Shape):

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        self.id = self.canvas.create_oval(
            self.x,
            self.y,
            self.x+self.size,
            self.y+self.size,
            fill=self.color,
            outline=self.outline
        )


# ==============================
# Rectangle Class
# ==============================
class Rectangle(Shape):

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        self.id = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x+self.size,
            self.y+self.size,
            fill=self.color,
            outline=self.outline
        )


# ==============================
# Canvas with Animation
# ==============================
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

        for i in range(num_shapes):

            if i % 2 == 0:
                shape = Ball(self,width,height,color,outline)
            else:
                shape = Rectangle(self,width,height,color,outline)

            self.shapes.append(shape)

        self.animate()


    def animate(self):

        for shape in self.shapes:
            shape.move()

        self.after(8,self.animate)


    def set_speed(self,speed):

        for shape in self.shapes:
            shape.speed_multiplier = speed


    def set_color(self,color):

        for shape in self.shapes:
            self.itemconfig(shape.id,fill=color)



# ==============================
# Config Panel
# ==============================
class ConfigPanel(tk.LabelFrame):

    def __init__(self, master, canvas, title):

        super().__init__(master,text=title,padx=5,pady=5)

        self.canvas = canvas

        tk.Label(self,text="Speed Multiplier:").pack()

        self.speed = tk.Scale(
            self,
            from_=-5,
            to=5,
            resolution=0.1,
            orient="horizontal",
            command=self.update_speed
        )

        self.speed.set(1)
        self.speed.pack()

        tk.Label(self,text="Select Color:").pack()

        self.color_var = tk.StringVar(value="orange")

        colors = ["orange","blue","green","purple"]

        for c in colors:

            tk.Radiobutton(
                self,
                text=c.capitalize(),
                value=c,
                variable=self.color_var,
                command=self.update_color
            ).pack(anchor="w")


    def update_speed(self,value):

        self.canvas.set_speed(float(value))


    def update_color(self):

        self.canvas.set_color(self.color_var.get())



# ==============================
# MAIN GUI
# ==============================
def main():

    root = tk.Tk()
    root.title("Interactive Multi-Canvas Bouncing Shapes")

    # LEFT CONTROL PANEL
    left_frame = tk.Frame(root,bg="white")
    left_frame.grid(row=0,column=0,sticky="ns",padx=10,pady=10)

    # RIGHT CANVAS GRID
    right_frame = tk.Frame(root)
    right_frame.grid(row=0,column=1,sticky="nsew")

    root.grid_columnconfigure(1,weight=1)
    root.grid_rowconfigure(0,weight=1)


    # CREATE CANVASES
    c1 = BouncingShapeCanvas(right_frame,color="#FF9800",outline="#E65100")
    c1.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)

    c2 = BouncingShapeCanvas(right_frame,color="#2196F3",outline="#1565C0")
    c2.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)

    c3 = BouncingShapeCanvas(right_frame,color="#4CAF50",outline="#2E7D32")
    c3.grid(row=1,column=0,sticky="nsew",padx=5,pady=5)

    c4 = BouncingShapeCanvas(right_frame,color="#9C27B0",outline="#6A1B9A")
    c4.grid(row=1,column=1,sticky="nsew",padx=5,pady=5)


    # RESIZE GRID
    right_frame.grid_rowconfigure(0,weight=1)
    right_frame.grid_rowconfigure(1,weight=1)
    right_frame.grid_columnconfigure(0,weight=1)
    right_frame.grid_columnconfigure(1,weight=1)


    # CONFIG PANELS
    ConfigPanel(left_frame,c1,"Panel 1 Config").pack(fill="x",pady=5)
    ConfigPanel(left_frame,c2,"Panel 2 Config").pack(fill="x",pady=5)
    ConfigPanel(left_frame,c3,"Panel 3 Config").pack(fill="x",pady=5)
    ConfigPanel(left_frame,c4,"Panel 4 Config").pack(fill="x",pady=5)


    root.mainloop()


# RUN PROGRAM
if __name__ == "__main__":
    main()