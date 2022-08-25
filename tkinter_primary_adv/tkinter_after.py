import tkinter

timer = 0  # 시간을 카운트 하는 변수

def count_up():
	global timer  # timer는 전역 변수
	timer += 1    # timer = timer + 1
	label["text"] = timer
	root.after(1000, count_up)  # 1초 뒤 다시 이 함수를 실행

root = tkinter.Tk()
label = tkinter.Label(font=("Time New Roman", 80))
label.pack()
root.after(1000, count_up)  # 첫 실행 지점(1초 후 지정 함수 실행)
root.mainloop()