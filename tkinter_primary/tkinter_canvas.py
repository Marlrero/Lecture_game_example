import tkinter as tk

root = tk.Tk()
root.title("캔버스 예")
canvas = tk.Canvas(root, width=400, height=600, bg="#000000")
canvas.pack()
root.mainloop()
