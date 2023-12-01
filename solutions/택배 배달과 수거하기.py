def solution(cap, n, deliveries, pickups):
    deliveries.reverse()
    pickups.reverse()

    answer = 0   
    box_d, box_p = 0, 0
    for i in range(n):
        box_d += deliveries[i]
        box_p += pickups[i]
        
        while box_d > 0 or box_p > 0:
            box_d -= cap
            box_p -= cap
            answer += (n - i) * 2
        
    return answer