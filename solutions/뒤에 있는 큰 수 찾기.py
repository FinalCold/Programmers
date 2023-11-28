def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, n in enumerate(numbers):
        while stack and stack[-1][1] < n:
            num = stack.pop()
            answer[num[0]] = n
        stack.append([i, n])
        
    return answer