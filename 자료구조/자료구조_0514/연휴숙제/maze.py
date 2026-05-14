def solve_maze(maze):
    # 미로 크기
    rows = len(maze)
    cols = len(maze[0])
    
    # 시작 위치 찾기
    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_pos = (r, c)
                break
    
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 스택 초기화 (좌표 저장)
    stack = [start_pos]
    # 방문 기록
    visited = set([start_pos])
    
    while stack:
        curr_r, curr_c = stack[-1]  # 현재 위치 (Stack Top)
        
        # 목적지 도착 여부 확인
        if maze[curr_r][curr_c] == 'E':
            print("탈출 성공!")
            return stack
        
        found_path = False
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            # 미로 범위 내에 있고, 벽(1)이 아니며, 방문하지 않은 곳인 경우
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '1' and (nr, nc) not in visited:
                    stack.append((nr, nc))
                    visited.add((nr, nc))
                    found_path = True
                    break  # 한 방향으로 깊게 탐색 (DFS)
        
        # 갈 곳이 없으면 스택에서 제거 (Backtracking)
        if not found_path:
            stack.pop()
            
    print("탈출구를 찾을 수 없습니다.")
    return None

# 미로 구성 (0: 길, 1: 벽, S: 시작, E: 종료)
maze_layout = [
    ['S', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', 'E'],
    ['1', '1', '1', '1', '1']
]

path = solve_maze(maze_layout)

if path:
    print("이동 경로:", path)