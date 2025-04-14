# 구현_문자열 재정렬.py
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열 입력으루 주어집니다.
# 이 때 모든 알파벳을 오름차순으로 정렬하여 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

input_data =input()
result =[]
value =0

for x in input_data:
    # 알파뱃이면 리스트에 추가
    if x.isalpha():
        result.append(x)
    # 알파벳이 아니면 값을 더함.
    else:
        value+=int(x)

# 오름차순 정렬
result.sort()
# 숫자가 있다면 마지막에 숫자 넣어
if value !=0:
    result.append(str(value))

#리스트를 문자열로 출력
print(''.join(result))