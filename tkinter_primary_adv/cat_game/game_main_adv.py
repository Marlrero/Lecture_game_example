import tkinter as tk
import random

root = tk.Tk()

index = 0  # 게임 진행 관련 인덱스
timer = 0  # 타이머
score = 0  # 점수
next_cat = 0  # 다음에 놓을 고양이

high_score = 1000 # 최고 점수용
difficulty = 0    # 난이도

BG_SIZE = (912, 768)
CUR_LIMIT = 24
BLOCK_SIZE = (8, 10)
BLOCK_PIXEL = 72
IMG_CAT = [
    None, # 0은 아무것도 없음(cat_loc에서)
    tk.PhotoImage(file="resource/neko1.png"),
    tk.PhotoImage(file="resource/neko2.png"),
    tk.PhotoImage(file="resource/neko3.png"),
    tk.PhotoImage(file="resource/neko4.png"),
    tk.PhotoImage(file="resource/neko5.png"),
    tk.PhotoImage(file="resource/neko6.png"),
    tk.PhotoImage(file="resource/neko_niku.png")
]

cat_loc = []
check = []  # 판정용 리스트
for i in range(BLOCK_SIZE[1]):
    cat_loc.append([0*x for x in range(BLOCK_SIZE[0])])
    check.append([0*x for x in range(BLOCK_SIZE[0])])

cursor_x = 0  # 커서의 좌표
cursor_y = 0
mouse_x = 0   # 실제 마우스 좌표
mouse_y = 0
mouse_c = 0   # 실제 마우스 클릭 여부

def mouse_move(e): # 마우스 움직일 때 이벤트 함수
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e): # 마우스 클릭 시 이벤트 함수
    global mouse_c
    mouse_c = 1

def drop_cat(): # 고양이가 위에서 떨어져야 함
    flag = False  # 낙하 여부 (떨어지지 않았음)
    for y in range(BLOCK_SIZE[0], -1, -1): # 8부터 0까지 1씩 감소
        for x in range(BLOCK_SIZE[0]):   # 0부터 7까지 1씩 증가
            # 고양이가 있어야 하고, 아래로 내려갈 때 비어 있으면
            if cat_loc[y][x] != 0 and cat_loc[y + 1][x] == 0:
                cat_loc[y + 1][x] = cat_loc[y][x] # 아래로 내려가
                cat_loc[y][x] = 0 # 원래 있던 곳은 고양이가 없어짐
                flag = True  # 고양이가 떨어진 것임
    return flag

def draw_cat(): # 고양이를 그리는 함수
    cvs.delete("CAT")
    for y in range(BLOCK_SIZE[1]):
        for x in range(BLOCK_SIZE[0]):
            if cat_loc[y][x] > 0:
                cvs.create_image(x*BLOCK_PIXEL + 60, y*BLOCK_PIXEL + 60, \
                    image=IMG_CAT[cat_loc[y][x]], tag="CAT")

def decide_cat():  # 고양이 3마리 판별
    # 판정용 리스트로 복사하기 (주의: check = cat_loc로 안됨!)
    for y in range(BLOCK_SIZE[1]):
        for x in range(BLOCK_SIZE[0]):
            check[y][x] = cat_loc[y][x]    
    
    # 가로 판정 코드
    for y in range(BLOCK_SIZE[1]):
        for x in range(1, BLOCK_SIZE[0] - 1): # x는 1~7
            if check[y][x] > 0: # 고양이가 아닌 경우 제외
                if check[y][x - 1] == check[y][x] == check[y][x + 1]:
                    cat_loc[y][x - 1] = cat_loc[y][x] = cat_loc[y][x + 1] = 7
    
    # 세로 판정 코드
    for y in range(1, BLOCK_SIZE[1] - 1): # y는 1~9
        for x in range(BLOCK_SIZE[0]):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] == check[y + 1][x]:
                    cat_loc[y - 1][x] = cat_loc[y][x] = cat_loc[y + 1][x] = 7
    
    # 대각선 판정 코드
    for y in range(1, BLOCK_SIZE[1] - 1): # y는 1~9
        for x in range(1, BLOCK_SIZE[0] - 1): # x는 1~7
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] == check[y + 1][x + 1]:
                    cat_loc[y - 1][x - 1] = cat_loc[y][x] = cat_loc[y + 1][x + 1] = 7
                    
                if check[y + 1][x - 1] == check[y][x] == check[y - 1][x + 1]:
                    cat_loc[y + 1][x - 1] = cat_loc[y][x] = cat_loc[y - 1][x + 1] = 7

def footprint_delete():  # 발자국 제거
    num = 0  # 지워야 할 발자국 카운트 (점수 계산 위해)
    for y in range(BLOCK_SIZE[1]):
        for x in range(BLOCK_SIZE[0]):
            if cat_loc[y][x] == 7:
                cat_loc[y][x] = 0
                num += 1
                
    return num

def over_cat_line():  # 맨 윗줄에 도달했는가?
    for x in range(BLOCK_SIZE[0]):
        if cat_loc[0][x] > 0: # 맨 윗줄이면 y가 0일 때임
            return True  
    return False

def top_line_cat(): # 맨 윗 줄에 고양이를 놓는 경우
    for x in range(BLOCK_SIZE[0]):
        cat_loc[0][x] = random.randint(0, difficulty) # 난이도를 여기서 정해줌. 위에서 뿌림.
        
def draw_txt(txt, x, y, size, color, tag):
    fnt = ("Times New Roman", size, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tag) # 그림자
    cvs.create_text(x, y, text=txt, fill=color, font=fnt, tag=tag)
                
# 60 pixel 더하기: create_image의 좌표가 이미지의 중심좌표이므로
# 여백의 24픽셀과 블록 픽셀 72의 절반인 36픽셀을 더해서 60픽셀을 사용함
def main_action(): # 실시간 처리 함수
    global cursor_x, cursor_y, mouse_c
    global index, timer, score, next_cat, high_score, difficulty

    if index == 0: # 타이틀 로고
        draw_txt("Cat game!", 312, 240, 100, "violet", "TITLE")
        #draw_txt("Click to start.", 312, 560, 50, "orange", "TITLE")
        
        # 난이도 설정 추가
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        
        index = 1
        mouse_c = 0
    elif index == 1: # 타이틀 화면, 시작 대기
        difficulty = 0
        
        if mouse_c == 1: # 클릭하면
            # 난이도 어떤 버튼 눌렀는지 체크
            if 168 < mouse_x < 456 and 384 < mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x < 456 and 528 < mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x < 456 and 672 < mouse_y < 744:
                difficulty = 6
            
            if difficulty > 0:
                # 고양이 위치 관리 초기화
                for y in range(BLOCK_SIZE[1]):
                    for x in range(BLOCK_SIZE[0]):
                        cat_loc[y][x] = 0
                
                mouse_c = 0
                score = 0
                next_cat = 0
                cursor_x = cursor_y = 0
                top_line_cat()
                draw_cat()
                cvs.delete("TITLE") # 타이틀 제거
                index = 2
                
    elif index == 2: # 고양이 낙하
        if drop_cat() == False: # 낙하할 고양이가 없으면
            index = 3
        draw_cat()
    elif index == 3: # 고양이가 나란히 놓였는지 판정
        decide_cat()
        draw_cat()
        index = 4
    elif index == 4: # 나란히 놓인 고양이가 있으면 삭제
        sc = footprint_delete()  # 발자국 삭제하고, 몇 개 발자국이 없어졌는지 담기
        #score += sc*10  # 발자국 1개당 10점씩 추가
        score += sc * difficulty * 2  # 난이도마다 가산점 부여
        if score > high_score:  # 최고점수를 넘기면 
            high_score = score
            
        if sc > 0:    # 삭제한 발자국이 있다면
            index = 2
        else:
            if over_cat_line() == False: # 가장 윗줄에 도달하지 않으면
                #next_cat = random.randint(1, 6) # 다음 고양이를 랜덤하게 정함
                next_cat = random.randint(1, difficulty) # 난이도 추가
                index = 5
            else:  # 가장 윗줄에 도달했다면
                index = 6  # 게임 오버
                timer = 0  # 타이머 초기화
                
        draw_cat()
    elif index == 5: # 마우스 입력 대기   
        if CUR_LIMIT <= mouse_x < CUR_LIMIT + BLOCK_PIXEL * BLOCK_SIZE[0] \
            and CUR_LIMIT <= mouse_y < CUR_LIMIT + BLOCK_PIXEL * BLOCK_SIZE[1]:
            cursor_x = int((mouse_x - CUR_LIMIT) / BLOCK_PIXEL)
            cursor_y = int((mouse_y - CUR_LIMIT) / BLOCK_PIXEL)
            if mouse_c == 1: # 마우스를 클릭했으면
                mouse_c = 0  # 마우스 클릭 변수 초기화
                top_line_cat() # 가장 윗줄 고양이 설정
                cat_loc[cursor_y][cursor_x] = next_cat # 현재 커서에 고양이 놓기
                next_cat = 0
                index = 2
                
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * BLOCK_PIXEL + 60, cursor_y * BLOCK_PIXEL + 60,\
                         image=cursor, tag="CURSOR")
        draw_cat()
    elif index == 6: # 게임 오버
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50: # 5초 뒤면 (0.1s * 50 = 5s)
            cvs.delete("OVER")
            index = 0  # 초기로 돌아감
            
    cvs.delete("INFO")  # 점수표시 삭제
    draw_txt("SCORE: " + str(score), 160, 60, 32, "blue", tag="INFO")
    # 최고점수 추가
    draw_txt("HIGH: " + str(high_score), 450, 60, 32, "yellow", "INFO")
    if next_cat > 0: # 다음에 배치할 고양이가 있다면
        cvs.create_image(752, 128, image=IMG_CAT[next_cat], tag="INFO")
    root.after(100, main_action)
    
root.title("AniPang")
root.resizable(False, False)
cvs = tk.Canvas(root, width=BG_SIZE[0], height=BG_SIZE[1]) # background size
cvs.pack()

# 경로 설정 잘해야 함!
background = tk.PhotoImage(file="resource/neko_bg.png")
cursor = tk.PhotoImage(file="resource/neko_cursor.png")
cvs.create_image(BG_SIZE[0] // 2, BG_SIZE[1] // 2, image=background)

root.bind("<Motion>", mouse_move) # 마우스 이벤트 처리
root.bind("<ButtonPress>", mouse_press)
main_action()  # 실시간 처리 함수 시작점
root.mainloop()