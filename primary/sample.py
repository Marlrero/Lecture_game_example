from random import randint   
# import random으로 쓰면 random.randint(1, 6)으로 써야 함

player_pos = 1
computer_pos = 1

def board(name, pos):
	print('*' * (pos – 1) + name + "*" * (30 – pos) + "V")

print("Game Start!")
board("P", player_pos)
board("C", computer_pos)

while True:
    input("Enter 키를 입력하면 플레이어의 말이 움직여요~")
    player_rand = randint(1, 6)
    print("Player:", player_rand)
    player_pos += player_rand
    
    if player_pos >= 30:
        player_pos = 30
        
    board("P", player_pos)
    if player_pos >= 30:   # 난수가 30이 넘어가면 이긴 것으로 판정
        print("Player 승리!")
        break

# while 문 안임 (이전 페이지 이어서)
    input("Enter 키를 입력하면 컴퓨터의 말이 움직여요~")
    computer_rand = randint(1, 6)
    print("Computer:", computer_rand)
    computer_pos += computer_rand
    
    if computer_pos >= 30:
        computer_pos = 30
        
    board("C", computer_pos)
    if computer_pos == 30:   # 난수가 30이 넘어가면 이긴 것으로 판정
        print("Computer 승리!")
        break

