import tkinter as tk

def check():
    if check_val.get() == True:
        print("체크되어 있음")
    else:
        print("체크되어 있지 않음")
        
def check2():
    if check_val2.get() == True:
        print("체크되어 있음22")
    else:
        print("체크되어 있지 않음22")
        
root = tk.Tk()
root.title("체크박스")
root.geometry("400x200")

check_val = tk.BooleanVar()
check_val.set(False)

check_btn = tk.Checkbutton(text="체크버튼", variable=check_val,
                           command=check)
check_btn.pack()

check_val2 = tk.BooleanVar()
check_val2.set(True)

check_btn2 = tk.Checkbutton(text="체크", variable=check_val2,
                           command=check2)
check_btn2.pack()

root.mainloop()