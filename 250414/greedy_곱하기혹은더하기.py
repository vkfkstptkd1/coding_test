# greedy_곱하기혹은더하기.py
# 각 자리가 숫자 (0-9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 연산자 '+'를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성해보세요.
# 단 기존 연산방식과 달리, 모든 연산은 왼쪽부터 순서대로 이루어진다고 가정합니다.


s = input()
result=int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if num <=1 or result <=1:
       result += num
    else:
       result *= num

print(result)


