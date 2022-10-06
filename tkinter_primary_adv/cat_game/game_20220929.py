import tkinter as tk

BG_SIZE = (912, 768)
CUR_LIMIT = 24
BLOCK_SIZE = (8, 10)
BLOCK_PIXEL = 72

cursor_x = 0  # 커서의 좌표
cursor_y = 0
mouse_x = 0   # 실제 마우스 좌표
mouse_y = 0

def mouse_move(e): # 마우스 움직일 때 이벤트 함수
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def main_action(): # 실시간 처리 함수
    global cursor_x, cursor_y
    if CUR_LIMIT <= mouse_x < CUR_LIMIT + BLOCK_PIXEL * BLOCK_SIZE[0] \
        and CUR_LIMIT <= mouse_y < CUR_LIMIT + BLOCK_PIXEL * BLOCK_SIZE[1]:
        cursor_x = int((mouse_x - CUR_LIMIT) / BLOCK_PIXEL)
        cursor_y = int((mouse_y - CUR_LIMIT) / BLOCK_PIXEL)
    
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x * BLOCK_PIXEL + 60, cursor_y * BLOCK_PIXEL + 60,\
                     image=cursor, tag="CURSOR")
    root.after(100, main_action)


root = tk.Tk()

IMG_CAT = [
    None,      # 0은 아무것도 없음(cat_loc에서)
    tk.PhotoImage(file="resource/neko1.png"),
    tk.PhotoImage(file="resource/neko2.png"),
    tk.PhotoImage(file="resource/neko3.png"),
    tk.PhotoImage(file="resource/neko4.png"),
    tk.PhotoImage(file="resource/neko5.png"),
    tk.PhotoImage(file="resource/neko6.png"),
    tk.PhotoImage(file="resource/neko_niku.png")
]

root.title("AniPang")
root.resizable(False, False)
cvs = tk.Canvas(root, width=BG_SIZE[0], height=BG_SIZE[1]) # background size
cvs.pack()

# 경로 설정 잘해야 함!
background = tk.PhotoImage(file="resource/neko_bg.png")
cursor = tk.PhotoImage(file="resource/neko_cursor.png")
cvs.create_image(BG_SIZE[0] // 2, BG_SIZE[1] // 2, image=background)

root.bind("<Motion>", mouse_move) # 마우스 이벤트 처리
main_action()  # 실시간 처리 함수 시작점

root.mainloop()