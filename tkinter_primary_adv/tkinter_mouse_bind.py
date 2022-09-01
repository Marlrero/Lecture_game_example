import tkinter

mouse_x = 0  # 마우스 포인터 x좌표
mouse_y = 0  # 마우스 포인터 y좌표
mouse_c = 0  # 마우스 포인터 클릭 여부(flag)

def mouse_move(e):  # 마우스 포인터 이동 시
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e): # 마우스 버튼 클릭 시
    global mouse_c
    mouse_c = 1

def mouse_release(e): # 마우스 버튼 클릭 후 해제 시
    global mouse_c
    mouse_c = 0

def main():
    _font = ("Time New Roman", 20)
    txt = f"mouse({mouse_x}, {mouse_y}) {mouse_c}"
    cvs.delete("TEST")  # 캔버스의 텍스트 태그 TEST를 지우기
    cvs.create_text(456, 384, text=txt, fill="black", font=_font, tag="TEST")
    root.after(100, main)  # 0.1초 후 이 함수 재실행

root = tkinter.Tk()
root.title("마우스 입력 이벤트")
root.resizable(False, False)  # 윈도우 크기 변경 불가

root.bind("<Motion>", mouse_move) # 마우스 포인터 이동 시 이벤트 등록
root.bind("<ButtonPress>", mouse_press) # 마우스 버튼 클릭 시 이벤트 등록
root.bind("<ButtonRelease>", mouse_release) # 마우스 버튼 클릭 후 해제 시 이벤트 등록

cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
main() # 실시간 처리 after 함수 시작점
root.mainloop()