# [문제]
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
# 예를 들어 1을 입력했을 때, 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# 00시 00분 03초
# 00시 13분 30초
# [입력] 첫째 줄에 정수 N이 입력됩니다. (0<=N<=23)
# [출력] 00시 00분 00초부터 N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수 출력

# 윤진아이디어
# 00 00 00 ~ N 59 59 까지 3을 포함하면 count+1

n = int(input())
count = 0
s=''
for i in range (n+1):
    for j in range (60):
        for k in range (60):
            s= str(i)+str(j)+str(k)
            if '3' in s :
                count+=1
print(count)




# # 구현: 완전탐색(brute Force)
# n = int(input())
# count =0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count+=1
# print(count)
#