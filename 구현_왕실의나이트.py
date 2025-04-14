#구현_왕실의나이트.py
# 정원: 8x8 좌표평면. 왕실 정원의 특정 한 칸에 나이트가 서있다.
# L자 형태로만 이동가능하며 정원 밖으로 나갈 수 없다.
# 이동방법
# 1. 수평으로 두칸 이동 뒤 수직으로 한칸 이동
# 2. 수직으로 두칸 이동 뒤 수평으로 한칸 이동
# 특정 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수는? 
# 행 위치는 1~8, 열 위치는 a~h 로 표현한다.
# 입력 예시는 a1, 출력예시는 2

input_data=input()
sx=int(input_data[1])
sy=int(ord(input_data[0])) -ord('a') +1

count =0
# 이동할 수 있는 방향을 정의한다.
move_types=[(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
for move in move_types:
    nx=sx+move[0]
    ny=sx+move[1]
    if nx <1 or nx >8 or ny <1 or ny> 8:
        continue
    count+=1
print(count)

# input_data=input()
# row= int(input_data[1])
# column= int(ord(input_data[0]))-int(ord('a'))+1 # 입력 아스키 - a 아스키 + 1 = 열의 위치

# moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]

# result = 0
# for move in moves:
#     next_row= row + move[0]
#     next_column=column+move[1]
#     if next_row >=1 and next_row <=8 and next_column >= 1 and next_column <=8:
#         result+=1

# print(result)
    
