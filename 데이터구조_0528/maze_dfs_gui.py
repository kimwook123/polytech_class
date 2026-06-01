import random
import tkinter as tk
from tkinter import messagebox


class MazeDFSGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DFS 미로 탐색")
        self.geometry("760x620")
        self.resizable(False, False)

        self.cell_size = 40
        self.size_var = tk.IntVar(value=10)

        self.maze = []
        self.rows = 0
        self.cols = 0
        self.start = (0, 0)
        self.goal = (0, 0)

        self.status = tk.StringVar(value="미로 탐색을 시작하세요")
        self.visited_cells = set()
        self.path_cells = set()
        self.pending_path = []
        self.animation_job = None

        self._build_ui()
        self.generate_random_maze()

    def _build_ui(self):
        top_frame = tk.Frame(self, padx=12, pady=12, bg="#f0f0f0")
        top_frame.pack(fill="x")

        title = tk.Label(
            top_frame,
            text="깊이 우선 탐색(DFS) 미로 탐색",
            font=("Segoe UI", 16, "bold"),
            bg="#f0f0f0",
            anchor="w",
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            top_frame,
            text="스택을 이용해 탐색하고, 경로를 시각화합니다.",
            font=("Segoe UI", 10),
            bg="#f0f0f0",
            anchor="w",
        )
        subtitle.pack(anchor="w")

        status = tk.Label(
            top_frame,
            textvariable=self.status,
            font=("Segoe UI", 10, "bold"),
            bg="#f0f0f0",
            fg="#1f4d9f",
            anchor="w",
        )
        status.pack(anchor="w", pady=(6, 0))

        control_frame = tk.Frame(self, padx=12, pady=12, bg="#fafafa")
        control_frame.pack(fill="x")

        self.run_button = tk.Button(
            control_frame,
            text="탐색 시작",
            font=("Segoe UI", 10, "bold"),
            command=self.start_search,
            width=14,
        )
        self.run_button.pack(side="left", padx=(0, 8))

        size_label = tk.Label(
            control_frame,
            text="크기",
            font=("Segoe UI", 10, "bold"),
            bg="#fafafa",
        )
        size_label.pack(side="left", padx=(8, 4))

        self.size_spinbox = tk.Spinbox(
            control_frame,
            from_=6,
            to=12,
            textvariable=self.size_var,
            width=4,
            font=("Segoe UI", 10),
        )
        self.size_spinbox.pack(side="left")

        random_button = tk.Button(
            control_frame,
            text="랜덤 미로 생성",
            font=("Segoe UI", 10, "bold"),
            command=self.generate_random_maze,
            width=16,
        )
        random_button.pack(side="left", padx=(8, 0))

        reset_button = tk.Button(
            control_frame,
            text="초기화",
            font=("Segoe UI", 10, "bold"),
            command=self.reset_maze,
            width=14,
        )
        reset_button.pack(side="left", padx=(8, 0))

        self.canvas = tk.Canvas(
            self,
            width=self.cols * self.cell_size + 2,
            height=self.rows * self.cell_size + 2,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.canvas.pack(padx=12, pady=12)

    def draw_maze(self):
        self.canvas.delete("all")
        self.cell_rects = {}
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "#2c2f33" if self.maze[r][c] == 1 else "#ffffff"
                rect = self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="#d0d7de",
                    width=1,
                )
                self.cell_rects[(r, c)] = rect

        self.canvas.configure(
            width=self.cols * self.cell_size + 2,
            height=self.rows * self.cell_size + 2,
        )
        self.refresh_grid()

    def refresh_grid(self):
        for (r, c), rect in self.cell_rects.items():
            if (r, c) == self.start:
                fill = "#2ecc71"
            elif (r, c) == self.goal:
                fill = "#e74c3c"
            elif (r, c) in self.path_cells:
                fill = "#f1c40f"
            elif (r, c) in self.visited_cells:
                fill = "#87ceeb"
            elif self.maze[r][c] == 1:
                fill = "#2c2f33"
            else:
                fill = "#ffffff"

            self.canvas.itemconfig(rect, fill=fill)

    def reset_maze(self):
        if self.animation_job is not None:
            self.after_cancel(self.animation_job)
            self.animation_job = None

        self.visited_cells.clear()
        self.path_cells.clear()
        self.pending_path = []
        self.status.set("미로 탐색을 시작하세요")
        self.run_button.config(state="normal")
        self.refresh_grid()

    def generate_random_maze(self):
        size = int(self.size_var.get())
        max_retry = 30
        for _ in range(max_retry):
            maze = self._generate_random_maze(size)
            self.maze = maze
            self.rows = len(maze)
            self.cols = len(maze[0])
            # 입구/출구 좌표는 self.start, self.goal에 이미 반영됨
            steps, path = self.run_dfs()
            if path and path[0] == self.start and path[-1] == self.goal:
                break
        else:
            self.status.set(f"{size}x{size} 미로 생성 실패 (출구 없음)")
            self.draw_maze()
            return
        if self.animation_job is not None:
            self.after_cancel(self.animation_job)
            self.animation_job = None
        self.visited_cells.clear()
        self.path_cells.clear()
        self.pending_path = []
        self.status.set(f"{self.rows}x{self.cols} 랜덤 미로 생성 완료")
        self.run_button.config(state="normal")
        self.draw_maze()

    def _generate_random_maze(self, size):
        # 홀수 크기로 강제 (미로 구조상)
        if size % 2 == 0:
            size += 1
        maze = [[1 for _ in range(size)] for _ in range(size)]
        stack = []
        start = (1, 1)
        maze[start[0]][start[1]] = 0
        stack.append(start)
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        while stack:
            r, c = stack[-1]
            random.shuffle(directions)
            moved = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 1 <= nr < size-1 and 1 <= nc < size-1 and maze[nr][nc] == 1:
                    maze[nr][nc] = 0
                    maze[r + dr//2][c + dc//2] = 0
                    stack.append((nr, nc))
                    moved = True
                    break
            if not moved:
                stack.pop()
        # 입구/출구 강제 개방
        maze[1][1] = 0
        maze[size-2][size-2] = 0
        # 외곽은 벽, 시작/끝 좌표 조정
        self.start = (1, 1)
        self.goal = (size-2, size-2)
        return maze

    def start_search(self):
        if self.animation_job is not None:
            return

        self.reset_maze()
        self.run_button.config(state="disabled")
        self.status.set("DFS 탐색 중...")

        self.search_steps, self.solution_path = self.run_dfs()
        self.animate_search()

    def run_dfs(self):
        stack = [self.start]
        parents = {self.start: None}
        visited = set()
        visited_order = []

        while stack:
            current = stack[-1]
            if current == self.goal:
                path = []
                cell = current
                while cell is not None:
                    path.append(cell)
                    cell = parents[cell]
                path.reverse()
                return visited_order, path

            if current not in visited:
                visited.add(current)
                visited_order.append(current)

            moves = self.get_valid_moves(current)
            moved = False
            for nxt in moves:
                if nxt not in visited:
                    parents[nxt] = current
                    stack.append(nxt)
                    moved = True
                    break

            if not moved:
                stack.pop()

        return visited_order, []

    def get_valid_moves(self, cell):
        r, c = cell
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        next_cells = []
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.maze[nr][nc] == 0:
                    next_cells.append((nr, nc))
        return next_cells

    def animate_search(self):
        if not self.search_steps:
            if self.solution_path:
                self.status.set("경로를 표시합니다")
                self.pending_path = self.solution_path
                self.animate_path()
            else:
                self.status.set("경로를 찾지 못했습니다")
                messagebox.showinfo("미로 탐색", "도착 지점까지 경로를 찾지 못했습니다.")
                self.run_button.config(state="normal")
            return

        cell = self.search_steps.pop(0)
        self.visited_cells.add(cell)
        self.refresh_grid()
        self.animation_job = self.after(140, self.animate_search)

    def animate_path(self):
        if not self.pending_path:
            self.status.set("탐색 완료")
            self.run_button.config(state="normal")
            self.animation_job = None
            return

        cell = self.pending_path.pop(0)
        self.path_cells.add(cell)
        self.refresh_grid()
        self.animation_job = self.after(160, self.animate_path)


if __name__ == "__main__":
    app = MazeDFSGUI()
    app.mainloop()
