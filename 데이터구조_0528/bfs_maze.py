from collections import deque

def bfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # 상, 하, 좌, 우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    queue = deque([(start[0], start[1], [])]) # (y, x, 지금까지의 경로)
    visited = set()
    visited.add(start)

    while queue:
        y, x, path = queue.popleft()
        path = path + [(y, x)]

        if (y, x) == end:
            return path

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 미로 범위 내에 있고, 벽(1)이 아니며, 방문하지 않은 곳
            if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] == 0 and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, path))
                
    return None # 경로를 찾지 못함


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

    print("=== BFS 미로 탐색 경로 ===")
    print(bfs_maze(maze, start_pos, end_pos))