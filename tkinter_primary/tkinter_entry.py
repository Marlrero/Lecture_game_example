import tkinter as tk

def click_btn():
    txt = entry.get()
    btn["text"] = txt

root = tk.Tk()
root.title("입력 필드")
root.geometry("400x200")

entry = tk.Entry(width=30)
entry.place(x=10, y=10)

btn = tk.Button(text="클릭", command=click_btn)
btn.place(x=20, y=100)

root.mainloop()