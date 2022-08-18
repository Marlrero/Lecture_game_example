import tkinter as tk
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("정보", "버튼 클릭!")

root = tk.Tk()
root.title("메시지박스")
root.geometry("400x200")

btn = tk.Button(text="test", command=click_btn)
btn.pack()

root.mainloop()