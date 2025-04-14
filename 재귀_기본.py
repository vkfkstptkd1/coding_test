# 재귀_기본.py



def factorial(i):
    if i<=1: return 1
    return i * factorial(i-1)

factorial(5)
