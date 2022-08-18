import tkinter as tk

def check():
    if check_val.get() == True:
        print("체크되어 있음")
    else:
        print("체크되어 있지 않음")
        
root = tk.Tk()
root.title("체크박스")
root.geometry("400x200")

check_val = tk.BooleanVar()
check_val.set(False)

check_btn = tk.Checkbutton(text="체크버튼", variable=check_val,
                           command=check)
check_btn.pack()

root.mainloop()