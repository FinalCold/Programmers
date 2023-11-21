def to_min(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    array = []
    for s, e in book_time:
        s = to_min(s)
        e = to_min(e) + 10
        array.append((s, 's'))
        array.append((e, 'e'))

    array.sort()
    count = 0
    max_room = 0
    for val, flag in array:
        if flag == 's':
            count += 1
        elif flag == 'e':
            count -= 1
        
        if count >= max_room:
            max_room = count

    return max_room
