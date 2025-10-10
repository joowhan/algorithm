import math

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    k -= 1  # 0-based index로 맞추기 위해 1 감소

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        answer.append(numbers.pop(index))
        k %= fact

    return answer
