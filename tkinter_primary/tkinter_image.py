import tkinter as tk

root = tk.Tk()
root.title("사진 넣기")
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack()

img = tk.PhotoImage(file="apple.gif")
   # file="이미지 경로"
canvas.create_image(200, 200, image=img)
   # x좌표, y좌표, image=이미지를 로딩한 변수

root.mainloop()
