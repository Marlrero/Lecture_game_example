import tkinter as tk  # tkinter 대신, tk라는 별명 사용

def click_btn():
	button["text"] = "2스테이지"

root = tk.Tk()
root.title("버튼 만들기")
root.geometry("800x600")

button = tk.Button(root, text="다음 스테이지 이동!", \
                    font=("Time New Roman", 24), \
				    command=click_btn)
button.place(x=200, y=100)

root.mainloop()
