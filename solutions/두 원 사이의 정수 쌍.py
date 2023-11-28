import math

# 피타고라스 정리 활용
def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        if r1 >= x:
            y1 = math.ceil((r1 ** 2 - x ** 2) ** 0.5)
        else:
            y1 = 0
        y2 = math.floor((r2 ** 2 - x ** 2) ** 0.5)
        print(y1, y2)
        dots = y2 - y1 + 1
        answer += dots

    return answer * 4