import heapq

def heuristic(a, b):
    # 맨해튼 거리 (Manhattan Distance) 계산
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 우선순위 큐: (예상 총 비용, 현재 비용, y, x, 경로)
    pq = []
    heapq.heappush(pq, (0, 0, start[0], start[1], []))
    
    # 방문 비용 기록
    costs = {start: 0}

    while pq:
        f_cost, g_cost, y, x, path = heapq.heappop(pq)
        path = path + [(y, x)]

        if (y, x) == end:
            return path

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] == 0:
                new_cost = g_cost + 1 # 이동 비용은 1
                
                # 처음 방문하거나, 더 짧은 경로를 찾았을 경우
                if (ny, nx) not in costs or new_cost < costs[(ny, nx)]:
                    costs[(ny, nx)] = new_cost
                    priority = new_cost + heuristic((ny, nx), end)
                    heapq.heappush(pq, (priority, new_cost, ny, nx, path))
                    
    return None

if __name__ == "__main__":
    # 0: 길, 1: 벽
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)

    print("\n=== A* (전략적) 미로 탐색 경로 ===")
    print(astar_maze(maze, start_pos, end_pos))