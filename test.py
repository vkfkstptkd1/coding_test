# 아침 합 - 저녁 합 최솟값
# 아침 합을 구해야하고
# 저녁 합을 구해야 한다. 
# 아침합에 따라 저녁 합은 달라진다. 
# 아침합이 나올 수 있는 경우의 수와 저녁의 합이 나올 수 있는 경우의 수를 모두 배열에 담앙서 처리하면 되겠다.

# 전체 콤비 - 아침 콤비 - (i,i) = 저녁 콤비
from itertools import combinations

n = int(input())
p_array=[]
for i in range (n):
    p_array.append(list(map(int,input().split())))
nums = [i for i in range (n)]
morning_works = list(combinations(nums, int(n/2)))



minus_arr=[]
for morning_work in morning_works:
    morning_sum = 0
    evening_sum = 0 
    evening_work = tuple(i for i in nums if i not in morning_work)
    morining_combis = list(combinations(morning_work,2))
    evening_combis = list(combinations(evening_work,2))
    for morining_combi in morining_combis:
        morning_sum+=p_array[morining_combi[0]][morining_combi[1]]+p_array[morining_combi[1]][morining_combi[0]]
    for evening_combi in evening_combis:
        evening_sum+=p_array[evening_combi[0]][evening_combi[1]]+p_array[evening_combi[1]][evening_combi[0]]
    if morning_sum > evening_sum : minus_arr.append(morning_sum-evening_sum)
    else : minus_arr.append(evening_sum-morning_sum)
    

print(min(minus_arr))
