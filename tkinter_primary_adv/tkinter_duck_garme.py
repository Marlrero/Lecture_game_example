import tkinter
from PIL import Image, ImageTk  # 이미지 리사이즈 (pip install pillow)

key = ""
def key_down(e):  # 키를 눌렀을 때
    global key
    key = e.keysym

def key_up(e):    # 키를 눌렀다가 땠을 때
    global key
    key = ""

duck_x = 400  # 오리의 x좌표
duck_y = 300  # 오리의 y좌표

def main_action():
    global duck_x, duck_y
    if key == "Up":  # 위 방향키를 누르면
        duck_y -= 20  # y좌표 20픽셀 감소(위로 이동)
    if key == "Down": # 아래 방향키를 누르면
        duck_y += 20  # y좌표 20픽셀 증가(아래로 이동)
    if key == "Left":  # 왼쪽 방향키를 누르면
        duck_x -= 20  # x좌표 20픽셀 감소(왼쪽으로 이동)
    if key == "Right": # 오른쪽 방향키를 누르면
        duck_x += 20  # x좌표 20팍샐 증가(오른쪽으로 이동)
    canvas.coords("DUCK", duck_x, duck_y)  # 이미지 새 위치로
    root.after(100, main_action) # 0.1초후 다시 실행

root = tkinter.Tk()
root.title("오리 움직이기 게임")
canvas = tkinter.Canvas(width=800, height=600, bg="skyblue")
canvas.pack()

duck_img = Image.open("duck.png")
resized_img = duck_img.resize((50, 50))
img = ImageTk.PhotoImage(resized_img)
canvas.create_image(duck_x, duck_y, image=img, tag="DUCK")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
main_action()
root.mainloop()