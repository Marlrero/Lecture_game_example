import tkinter as tk
import tkinter.messagebox

def click_btn():
    msg_txt = [
        '메롱',
        '안녕'
    ]
    for i in range(2):
        tkinter.messagebox.showerror("정보", msg_txt[i])

root = tk.Tk()
root.title("메시지박스")
root.geometry("400x200")

btn = tk.Button(text="test", command=click_btn)
btn.pack()

root.mainloop()