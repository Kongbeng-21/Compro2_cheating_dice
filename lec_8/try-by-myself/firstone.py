import tkinter as tk

click_count = 0

def btn_increase():
    global click_count 
    click_count += 1
    lbl.config(text=f"{click_count}",font=("Helvetica", 42),bg="white", fg="black")
    
def btn_decrease():
    global click_count 
    click_count -= 1
    lbl.config(text=f"{click_count}",font=("Helvetica", 42),bg="white", fg="black")
    
    
root = tk.Tk()
root.title("First")
root.geometry("800x400")

lbl = tk.Label(root, text="0", font=("Helvetica", 42), bg="white", fg="black")
lbl.pack(pady=20)
btn = tk.Button(root,text=("+1"),command=btn_increase,bg="white", fg="black")
btn.pack(pady=10)
btn = tk.Button(root,text=("-1"),command=btn_decrease,bg="white", fg="black")
btn.pack(pady=10)
root.mainloop()