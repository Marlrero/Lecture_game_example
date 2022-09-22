import tkinter

key = 0  # 키보드가 어떤 키가 입력됐는지 그 코드 값 저장
def key_down(e):
    global key
    #key = e.keycode
    key = e.keysym
    
    if key == 'w':
        print('위')
    elif key == 'a':   # else if -> elif
        print('왼쪽')
    elif key == 'd':
        print('오른쪽')
    elif key == 's':
        print('아래')
    
    print("Key input: " + str(key))

root = tkinter.Tk()
root.title("키보드 입력")
root.bind("<KeyPress>", key_down)
    # 키가 눌리면 key_down 함수를 실행하라
root.mainloop()