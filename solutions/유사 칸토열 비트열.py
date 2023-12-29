def solution(n, l, r):
    answer = f(n, r) - f(n, l - 1)
    return answer

def f(n, pos):
    if n == 1:
        return '11011'[:pos].count('1')
    quotient, remainder = divmod(pos, 5 ** (n - 1))
    cnt = 0
    if quotient <= 1:
        cnt = 4 ** (n - 1) * quotient + f(n - 1, remainder)
    elif quotient == 2:
        cnt = 2 * 4 ** (n - 1)
    elif quotient > 2:
        cnt = 4 ** (n - 1) * (quotient - 1) + f(n - 1, remainder)
    
    return cnt