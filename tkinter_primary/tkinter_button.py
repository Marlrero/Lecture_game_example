import tkinter as tk  # tkinter 대신, tk라는 별명 사용

root = tk.Tk()
root.title("버튼 만들기")
root.geometry("800x600")

button = tk.Button(root, text="Button", \
                   font=("Time New Roman", 24))
button.place(x=200, y=100)

root.mainloop()

