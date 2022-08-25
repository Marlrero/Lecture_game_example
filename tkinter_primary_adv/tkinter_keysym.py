import tkinter

key = ""  # 키 코드가 아닌 어떤 키가 눌렸는지에 관한 문자열
def key_down(e):
    global key
    key = e.keysym # 이 부분

def main_action():
    label["text"] = key
    root.after(100, main_action)
    
root = tkinter.Tk()
root.title("실시간으로 키 입력받기")
label = tkinter.Label(font=("Time New Roman", 50))
label.pack()

root.bind("<Key>", key_down)
main_action()
root.mainloop()