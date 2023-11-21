def solution(maps):
    rows, cols = len(maps), len(maps[0])
    start, end, distance = 0, 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    path = []
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    L = 0
    
    # 시작
    for i, x in enumerate(maps) :
        if 'S' in x :
            j = x.index('S')
            r, c, distance = i, j, 0
            visited[i][j] = 1
            
    # 첫 번째 BFS        
    while True :
        for i in range(4) :
            x = [r + dx[i], c + dy[i]]
            if 0 <= x[0] < rows and 0 <= x[1] < cols and not visited[x[0]][x[1]] and maps[x[0]][x[1]] != 'X':
                path.append([x[0], x[1], distance + 1])
                visited[x[0]][x[1]] = 1

        if len(path) != 0 :
            r, c, distance = path.pop(0)
        else :
            distance = -1
            break
            
        # 두 번째 BFS
        if not L and maps[r][c] == 'L':
            L = 1
            visited = [[0 for _ in range(cols)] for _ in range(rows)]
            visited[r][c] = 1
            path = []
            path.append([r, c, distance])
        
        if L and maps[r][c] == 'E':
            break
    
    return distance