# 구현_문자열재정렬.py
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력을 ㅗ주어집니다.
# 이때 모든 알파벳을 오름차 순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

input_data=input()

sum=0
result=[]

for input in input_data:
    if input.isalpha():
        result.append(input)
    else:
        sum+=int(input)

result.sort()

if sum!=0:
    result.append(str(sum))

print(''.join(result))

