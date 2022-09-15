import tkinter as tk
import tkinter.messagebox as msgbox
from PIL import Image, ImageTk  # pip install pillow (image resize)

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

# 강아지 위치 좌표
dog_x = 1
dog_y = 1
is_clear = 0  # 게임 클리어 판정 변수 추가

# 키보드 이벤트를 위한 변수와 이벤트 함수 추가
key = ""
def key_down(e): # 키를 누를 때 발생하는 이벤트 처리 함수
    global key   # key는 global(전역) 변수야! local(지역)로 쓰지마!
    key = e.keysym

def key_up(e):   # 키를 뗄 때 발생하는 이벤트 처리 함수
    global key
    key = ""
    
def main_action():
    global dog_x, dog_y, is_clear
    if key == "Shift_L" and is_clear > 1: # 왼쪽Shift키가 눌리고 2칸 이상 칠했으면
        canvas.delete("PAINT")
        dog_x = dog_y = 1
        is_clear = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0    
    
    if key == "Up" and maze[dog_y - 1][dog_x] == 0: # 위키를 누르고 통로이면
        dog_y -= 1  # 위로 한 칸 가기
    if key == "Down" and maze[dog_y + 1][dog_x] == 0:  # 아래키를 누르고 통로이면
        dog_y += 1  # 아래로 한 칸 가기
    if key == "Left" and maze[dog_y][dog_x - 1] == 0: # 왼쪽키를 누르고 통로이면
        dog_x -= 1  # 왼쪽으로 한 칸 가기
    if key == "Right" and maze[dog_y][dog_x + 1] == 0: # 오른쪽키를 누르고 통로이면
        dog_x += 1  # 오른쪽으로 한 칸 가기
    if maze[dog_y][dog_x] == 0: # 캐릭터가 있는 장소가 통로라면
        maze[dog_y][dog_x] = 2  # 리스트 값을 2로 변경하고 사각형 다시 그리기
        is_clear += 1  # 칠한 횟수 1 증가
        canvas.create_rectangle(dog_x*80, dog_y*80, dog_x*80 + 79, dog_y*80 + 79, fill="yellow", width=0, tag="PAINT")
    canvas.delete("DOG")  # 사각형을 그렸으니 그 장소에 있는 강아지가 안보이므로 삭제하고 다시 그리기
    canvas.create_image(dog_x*80 + 40, dog_y*80 + 40, image=dog, tag="DOG")
    #canvas.coords("DOG", dog_x*80 + 40, dog_y*80 + 40) # 새로운 위치로 이동 (80픽셀 움직임)
    
    if is_clear == 30: # 30개 칸이 모두 칠해졌으면
        canvas.update()
        msgbox.showinfo("Game Clear!", "모든 곳을 칠했습니다!")
    else: 
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

main_action()  # main_action 함수 첫 시작점
root.mainloop()