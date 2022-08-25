import tkinter

key = 0  # 키보드 코드 값(어떤 것을 눌렀는지)
def key_down(e):
    global key
    key = e.keycode

def main_action():
    label["text"] = key
    root.after(100, main_action) # 0.1초 후에 이 함수 다시 실행

root = tkinter.Tk()
root.title("실시간으로 키 입력받기")
label = tkinter.Label(font=("Time New Roman", 50))
label.pack()

root.bind("<Key>", key_down)
main_action()  # 처음 실시간 처리 시작 지점
root.mainloop()