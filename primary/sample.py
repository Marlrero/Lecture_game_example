from random import randint   
# import random으로 쓰면 random.randint(1, 6)으로 써야 함

player_pos = 1
computer_pos = 1

def board(name, pos):
	print('*' * (pos – 1) + name + "*" * (30 – pos))

while True:
	board("P", player_pos)
	board("C", computer_pos)
	input("Enter 키를 입력하면 말이 움직여요~")
	player_pos += randint(1, 6)
	computer_pos += randint(1, 6)
