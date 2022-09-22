import tkinter as tk
from PIL import Image, ImageTk
# 미로 설정
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 강아지 위치
dog_x = 1
dog_y = 1

# 키보드 이벤트를 위한 변수와 이벤트 함수 추가
key = ""
def key_down(e): # 키를 누를 때 발생하는 이벤트 처리 함수
    global key   # key는 global(전역) 변수야! local(지역)로 쓰지마!
    key = e.keysym

def key_up(e):   # 키를 뗄 때 발생하는 이벤트 처리 함수
    global key
    key = ""

def main_action():
    global dog_x, dog_y
    if key == "Up" and maze[dog_y - 1][dog_x] == 0: # 위키를 누르고 통로이면
        dog_y -= 1  # 위로 한 칸 가기
    if key == "Down" and maze[dog_y + 1][dog_x] == 0:  # 아래키를 누르고 통로이면
        dog_y += 1  # 아래로 한 칸 가기
    if key == "Left" and maze[dog_y][dog_x - 1] == 0: # 왼쪽키를 누르고 통로이면
        dog_x -= 1  # 왼쪽으로 한 칸 가기
    if key == "Right" and maze[dog_y][dog_x + 1] == 0: # 오른쪽키를 누르고 통로이면
        dog_x += 1  # 오른쪽으로 한 칸 가기
    canvas.coords("DOG", dog_x*80 + 40, dog_y*80 + 40) 
    # 새로운 위치로 이동 (80픽셀 움직임)
    root.after(200, main_action)  # 0.2초후 이 함수 재실행

root = tk.Tk()
root.title("Maze Game")
# 800x500 화면 구성 -> 화면 구성이 먼저임
canvas = tk.Canvas(width=800, height=560, bg="white")
canvas.pack()

# 키보드 이벤트 등록
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 아래부터 2차원 리스트를 사각형으로 뿌리기
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1: # 벽이면
            canvas.create_rectangle(x*80, y*80, x*80 + 80, y*80 + 80, fill="gray")
            
# 강아지를 미로 안에 넣어야 함
dog = Image.open("dog.png")
dog = dog.resize((80, 80)) # 이미지 크기는, 사각형 블록의 크기와 같아야 함
dog = ImageTk.PhotoImage(dog)
canvas.create_image(dog_x*80 + 40, dog_y*80 + 40, image=dog, tag="DOG")

main_action()
root.mainloop()