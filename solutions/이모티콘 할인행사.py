from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    n = len(users)
    m = len(emoticons)
    discount_rate = [10, 20, 30, 40]
    
    rate_list = list(product(discount_rate, repeat = m))
    
    for rate in rate_list:
        emoticon_plus = 0
        emoticon_purchase = 0
        for discount_ratio, price in users:
            total = 0
            for i in range(len(rate)):
                if rate[i] >= discount_ratio:
                    total += (emoticons[i] // 100 * (100 - rate[i]))
                    
            if total >= price:
                emoticon_plus += 1
            else:
                emoticon_purchase += total
        
        answer = max(answer, [emoticon_plus, emoticon_purchase])
    
    return answer