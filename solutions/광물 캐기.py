def solution(picks, minerals):
    answer = 0
    num = {'diamond': 0, 'iron': 1, 'stone': 2}
    # 각 곡괭이로 광물을 캘 때의 피로도
    fatigue = [[1, 1, 1], 
               [5, 1, 1], 
               [25, 5, 1]]
    # 캘 수 있는 해당 개수까지 슬라이싱
    minerals = minerals[:5 * sum(picks)]

    # 각 광물의 수 체크
    check = []

    idx = 0
    cnt = 1
    temp = [0, 0, 0]
    while idx < len(minerals):
        # 하나의 곡괭이로 캘수 있는 광물을 다 채웠다면 각 변수들 초기화
        if cnt > 5:
            check.append(temp)
            cnt = 1
            temp = [0, 0, 0]

        temp[num[minerals[idx]]] += 1
        cnt += 1
        idx += 1

    if temp:
        check.append(temp)
        
    # 다이아몬드, 철, 돌이 많은 순으로 정렬
    check.sort(key=lambda x: (x[2], x[1], x[0]))

    # pick 순서대로 해당 곡괭이 개수만큼 곡괭이 번호
    pick = []
    for i in range(3):
        pick += [i] * picks[i]

    p = 0
    for i in range(len(check)):
        for j in range(len(num)):
            # 하나의 곡괭이를 소진했을 때 발생하는 피로도 누적
            answer += fatigue[pick[p]][j] * check[i][j]
        p += 1

    return answer