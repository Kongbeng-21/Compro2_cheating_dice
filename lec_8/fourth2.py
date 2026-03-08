import tkinter as tk
import random

class Shape:
    def __init__(self, canvas, canvas_width, canvas_height, color, outline):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.size = random.randint(10, 30)
        
        # Random starting position
        self.x = random.randint(0, canvas_width - self.size)
        self.y = random.randint(0, canvas_height - self.size)
        
        # Random starting velocity
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        while abs(self.vx) < 0.3: self.vx = random.uniform(-2, 2)
        while abs(self.vy) < 0.3: self.vy = random.uniform(-2, 2)
        
        self.color = color
        self.outline = outline
        self.id = None

    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.vx = -self.vx
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.vy = -self.vy

class Ball(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = self.canvas.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size,
            fill=self.color, outline=self.outline
        )

class Rectangle(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = self.canvas.create_rectangle(
            self.x, self.y, self.x + self.size, self.y + self.size,
            fill=self.color, outline=self.outline
        )

class BouncingShapeCanvas(tk.Canvas):
    def __init__(self, master, width=400, height=300, color="orange", outline="red", num_shapes=50, **kwargs):
        super().__init__(master, width=width, height=height, bg="white", highlightthickness=1, highlightbackground="gray", **kwargs)
        
        self.width = width
        self.height = height
        
        # Create 50 objects: half balls, half rectangles
        self.shapes = []
        for i in range(num_shapes):
            if i % 2 == 0:
                self.shapes.append(Ball(self, self.width, self.height, color, outline))
            else:
                self.shapes.append(Rectangle(self, self.width, self.height, color, outline))
        
        self.animate()

    def animate(self):
        for shape in self.shapes:
            shape.move()
        self.after(8, self.animate)

def main():
    root = tk.Tk()
    root.title("Multi-Canvas OOP: Balls & Rectangles")

    # Grid layout: 2x2
    c1 = BouncingShapeCanvas(root, color="#FF9800", outline="#E65100") # Orange
    c1.grid(row=0, column=0, padx=5, pady=5)
    
    c2 = BouncingShapeCanvas(root, color="#2196F3", outline="#1565C0") # Blue
    c2.grid(row=0, column=1, padx=5, pady=5)
    
    c3 = BouncingShapeCanvas(root, color="#4CAF50", outline="#2E7D32") # Green
    c3.grid(row=1, column=0, padx=5, pady=5)
    
    c4 = BouncingShapeCanvas(root, color="#9C27B0", outline="#6A1B9A") # Purple
    c4.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()