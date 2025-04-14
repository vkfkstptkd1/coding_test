# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 
# 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
# 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

input_data = input()

# 왼쪽부터 차례대로 확인한 후, -가 등장하고 ~ 다음 -가 나오기 전까지 )

# 1. + 를 만난다 -> 그 이전까지 합을 구한다.
# 2. - 를 만난다 -> 그 이전까지 합을 구한다, 그 이후는 

target =''
sum_data=[]
minus_data=[]
meet_minus=False
for input in input_data:
    target+=input
    if not meet_minus and input == '+':
        sum_data.append(int(target[:-1]))
        target=''
    elif not meet_minus and input =='-':
        sum_data.append(int(target[:-1]))
        meet_minus=True    
        target=''
    elif meet_minus and input == '+':
        minus_data.append(int(target[:-1]))
        target=''
    elif meet_minus and input == '-':
        minus_data.append(int(target[:-1]))
        target=''
if meet_minus : minus_data.append(int(target))
else: sum_data.append(int(target))
print(sum(sum_data)-sum(minus_data))
    

# 지피티 답변
expr = input().split('-')
result = sum(map(int,expr[0].split('+')))
for e in expr[1:]:
    result -=sum(map(int,e.split('+')))
print(result)
