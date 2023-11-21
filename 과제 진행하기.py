def solution(plans):
    answer = []
    
    def convert_time(s):
        h, m = map(int, s.split(':'))
        return h * 60 + m
    
    plans = [(name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key = lambda x: x[1])

    # 남은 시간을 저장하는 stack
    stack = []
    for i, (name, start, playtime) in enumerate(plans):
        total = start + playtime
        if i + 1 < len(plans):
            next_plan = plans[i + 1][1]
            # 현재 과제를 마칠 수 없을 때
            if total > next_plan:
                remain_time = total - next_plan
                stack.append([name, remain_time])
            # 현재 과제를 마칠 수 있을 때
            else:
                answer.append(name)
                # 남은 시간
                left_time = next_plan - total
                # 남은 시간이 있고, stack에 과제가 있다면
                while stack and left_time > 0:
                    if left_time >= stack[-1][1]:
                        left_time -= stack[-1][1]
                        answer.append(stack.pop())[0]
                    else:
                        stack[-1][1] -= left_time
                        break
        else:
            answer.append(name)
    
    # stack에 남아있는 plan
    while stack:
        name, _ = stack.pop()
        answer.append(name)

    return answer