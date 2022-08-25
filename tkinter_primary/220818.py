import tkinter

root = tkinter.Tk()  # 창이 하나 만들어짐
root.title("ABCDEFG")
root.geometry("800x600")

#f = tkinter.font.Font("Time New Roman", 24)
label = tkinter.Label(root, text="안녕", font=("궁서", 50))
label.place(x=200, y=100)

btn = tkinter.Button(root, text="메롱", font=("궁서", 20))
btn.place(x=500, y= 100)

root.mainloop()