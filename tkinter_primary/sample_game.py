import tkinter as tk

def change_label():
    label["text"] = "메롱"

root = tk.Tk()
root.title("뽑기 프로그램")
root.resizable(False, False) # 윈도우 크기 고정
canvas = tk.Canvas(root, width=400, height=300, bg="skyblue")
canvas.pack()

#img = tk.PhotoImage(file="background.png")
#canvas.create_image(200, 150, image=img)

label = tk.Label(root, text="??", font=("Time New Roman", 60), bg="white")
label.place(x=150, y=50)

btn = tk.Button(root, text="뽑기", font=("Time New Roman", 30), fg="red", command=change_label)
btn.place(x=140, y=200)

root.mainloop()