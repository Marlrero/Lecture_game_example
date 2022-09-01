from datetime import datetime
import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

answer = random.choice(alpha)   # choice(alpha)
question = ''    # 처음에 아무것도 없는 빈 문자열 생성

for i in alpha:
	if i != answer:      # 정답이 아니면 (빠진 문자를 빼고 넣기)
		question += i    # question = question + i

print(question)

start = datetime.datetime.now()  # 현재 시간 측정
my = input('빠진 알파벳은?')
if answer == my:
	print('정답!')
	end = datetime.datetime.now()  # 이 때 현재 시간 측정
	print((end - start).seconds)   # end - start를 빼서 초로 바꾸기
else:
	print('오답!')
