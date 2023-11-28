def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: x[1])
    
    shoot = -1
    for target in targets:
        print(shoot)
        s, e = target
        if s > shoot:
            answer += 1
            shoot = e - 0.5
    
    return answer