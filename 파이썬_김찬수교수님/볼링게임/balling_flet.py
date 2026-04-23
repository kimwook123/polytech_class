import flet as ft
import asyncio
import random

class BowlingGame:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Flet Bowling Center - Optimized"
        self.page.window.width = 1200
        self.page.window.height = 800
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        
        self.init_game_data()
        self.build_ui()

    # 게임 데이터 구성
    def init_game_data(self):
        # 프레임 별 쓰러뜨린 핀 개수 기록 
        self.all_frames_record = []
        # 전체 투구 기록 리스트
        self.only_rolls = []
        # 현재 진행중인 프레임 회차
        self.current_frame = 1
        # 현재 레인 위 세워져 있는 핀 갯수
        self.alive_pins = 10
        # 게임 종료 여부 확인(True가 되면 재시작 가능)
        self.game_over = False

    def build_ui(self): # UI 구성
        # 점수판 UI
        self.score_cells = []
        self.acc_cells = []
        self.total_score_text = ft.Text("0", size=35, weight="bold", color=ft.Colors.BLUE_800)
        
        header_row = ft.Row(spacing=0) # 1부터 10까지의 프레임 번호
        symbol_row = ft.Row(spacing=0) # 투구별 결과가 들어갈 칸
        acc_row = ft.Row(spacing=0)    # 해당 프레임까지의 누적 점수

        for i in range(1, 11):
            header_row.controls.append(self.create_cell(str(i), ft.Colors.BLUE_GREY_100))
            s_cell = ft.Text("", size=14)
            self.score_cells.append(s_cell)
            symbol_row.controls.append(self.create_cell(s_cell))
            a_cell = ft.Text("", size=14, weight="bold")
            self.acc_cells.append(a_cell)
            acc_row.controls.append(self.create_cell(a_cell))

        header_row.controls.append(self.create_cell("TOTAL", ft.Colors.AMBER_100, width=80))
        symbol_row.controls.append(self.create_cell("", width=80))
        acc_row.controls.append(self.create_cell(self.total_score_text, width=80, height=60))

        # 애니메이션 레인 UI
        self.pin_coords = [ # 볼링 핀 세워져있는 것 표현
            (100, 150), (70, 125), (70, 175),
            (40, 100), (40, 150), (40, 200),
            (10, 75), (10, 125), (10, 175), (10, 225)
        ]
        
        self.pins = [] # ft.Icons를 담은 컨테이너 생성
        for t, l in self.pin_coords:
            p = ft.Container(
                content=ft.Icon(ft.Icons.STREETVIEW, color=ft.Colors.RED_ACCENT, size=25),
                width=30, height=30, top=t, left=l,
                # 핀이 쓰러질 때 튕기는 느낌 표현: BOUNCE_OUT 활용
                animate_rotation=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
                # 쓰러진 핀을 흐리게 만드는 함수: EASE_OUT 활용
                animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            )
            self.pins.append(p)

        self.ball = ft.Container(
            width=35, height=35, bgcolor=ft.Colors.INDIGO_900, border_radius=18,
            top=500, left=150,
            # 공이 앞으로 나가는 움직임 표현
            animate_position=ft.Animation(1200, ft.AnimationCurve.DECELERATE),
            # 공이 데굴데굴 구르는 회전 효과 표현
            animate_rotation=ft.Animation(1200, ft.AnimationCurve.LINEAR),
        )

        lane_stack = ft.Stack( # 바닥->핀->공 순으로 쌓아 올리는 함수
            controls=[
                ft.Container(width=340, height=580, bgcolor=ft.Colors.BROWN_50, border=ft.Border.all(2, ft.Colors.BROWN_200)),
                *self.pins,
                self.ball
            ],
            width=340, height=580,
        )

        # 컨트롤 섹션
        self.status_text = ft.Text("환영합니다! 공을 굴려주세요.", size=16, weight="bold")
        self.roll_button = ft.Button(
            "공 굴리기!", icon=ft.Icons.STREETVIEW, on_click=self.roll_ball_action, 
            height=50, width=150, bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE
        )
        self.restart_button = ft.Button(
            "다시 시작", icon=ft.Icons.REFRESH, on_click=self.restart_game_action, 
            visible=False, bgcolor=ft.Colors.ORANGE_800, color=ft.Colors.WHITE
        )
        self.page.add(
            ft.Row([ # 화면을 좌우 두 구역으로 나눔
                ft.Column([ # 레인 제목, 볼링 레인, 상태창 및 버튼
                    ft.Text("🎳 BOWLING LANE", size=20, weight="bold"),
                    lane_stack,
                    self.status_text,
                    ft.Row([self.roll_button, self.restart_button])
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.VerticalDivider(width=30), # 가로 구분 수직선
                ft.Column([ # 점수판 제목, 3단 점수판, 하단 알림 텍스트
                    ft.Text("📊 SCORE BOARD", size=20, weight="bold"),
                    header_row, symbol_row, acc_row,
                    ft.Container(height=20),
                    ft.Text("알림: 모든 투구가 끝난 뒤 점수가 최종 계산됩니다.", color=ft.Colors.GREY_600)
                ], expand=True)
            ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.START)
        )

    def create_cell(self, content, bgcolor=None, width=65, height=45):
        return ft.Container(
            content=content if isinstance(content, ft.Control) else ft.Text(content, weight="bold" if bgcolor else "normal"),
            border=ft.Border.all(1, ft.Colors.BLACK26),
            width=width, height=height,
            alignment=ft.Alignment.CENTER,
            bgcolor=bgcolor
        )

    async def roll_ball_action(self, e):
        if self.game_over: return
        self.roll_button.disabled = True # 공을 굴릴 때 중복으로 굴려지지 않도록 클릭을 막아둠
        self.page.update()

        # 공 굴리기
        self.ball.top = 100         # 핀 방향으로 이동
        self.ball.rotate = 10       # 회전 효과 부여
        self.page.update()          
        await asyncio.sleep(1.2)    # 공이 굴러가는 시간 1.2초
        # await를 활용하여, 이벤트가 동시에 일어날 수 있도록 구성함

        # 결과 처리
        knockdown = random.randint(0, self.alive_pins) # 남은 핀 중에 몇 개가 쓰러질지 랜덤
        active_pins = [p for p in self.pins if p.opacity != 0.3] # 서 있는 핀 골라내기
        to_knock = random.sample(active_pins, knockdown) # 해당 핀 중 랜덤 선택
        for p in to_knock:
            p.rotate = 1.6   # 옆으로 눕히는 효과
            p.opacity = 0.3  # 흐리게 만드는 효과
        
        self.ball.opacity = 0 # 핀과 부딪하고, 공을 없앰
        self.page.update()

        # 데이터 기록 (먼저 현재 상태 저장)
        prev_frame = self.current_frame # 점수 계산 전 현재 프레임 번호 저장
        self.process_score(knockdown)   # 쓰러진 개수 데이터 기록
        self.update_scoreboard_ui()     # 점수판 글자 갱신

        # 다음 투구 준비
        await asyncio.sleep(0.5)
        if not self.game_over:
            # 리셋 여부 판단
            # 프레임이 이미 넘어갔거나(스트라이크), 현재 프레임의 투구가 2회 이상일 때 리셋
            is_frame_ended = (self.current_frame > prev_frame) or (len(self.all_frames_record[prev_frame-1]) >= 2)
            
            if is_frame_ended or self.alive_pins == 0:
                await self.reset_lane_visuals() # 핀 다시 세우고 공을 가져옴(비동기 처리)
            else:
                # 같은 프레임 두 번째 투구 준비(공 다시 가져오기)
                self.ball.top = 500
                self.ball.rotate = 0
                self.ball.opacity = 1
            self.roll_button.disabled = False
        else:
            self.restart_button.visible = True
        self.page.update()

    # 점수 관련 함수
    def process_score(self, knockdown):
        self.only_rolls.append(knockdown) # 공을 굴릴 때마다 only_rolls에 숫자를 쌓음
        if len(self.all_frames_record) < self.current_frame:
            self.all_frames_record.append([knockdown]) # 새로운 프레임(게임) 생성
        else:
            self.all_frames_record[self.current_frame-1].append(knockdown) # 기존 프레임에 추가

        if self.current_frame < 10:
            # 스트라이크 처리
            if knockdown == 10 and len(self.all_frames_record[self.current_frame-1]) == 1:
                self.current_frame += 1
                self.alive_pins = 10
            # 2구까지 던졌을 때
            elif len(self.all_frames_record[self.current_frame-1]) == 2:
                self.current_frame += 1
                self.alive_pins = 10
            else:
                self.alive_pins -= knockdown
        else:
            # 10프레임 특수 상황
            rolls = self.all_frames_record[9]
            if len(rolls) == 1: # 10프레임 1 투구
                    # 스트라이크면 10개 다시 세우고, 아니면 남은 핀 계산
                self.alive_pins = 10 if knockdown == 10 else 10 - knockdown
            elif len(rolls) == 2: # 10프레임 2 투구
                if sum(rolls[:2]) >= 10: self.alive_pins = 10
                else: self.game_over = True
            else:
                self.game_over = True

    async def reset_lane_visuals(self):
        for p in self.pins:
            p.rotate = 0            # 넘어뜨린 핀 다시 세우기
            p.opacity = 1           # 투명한 핀 다시 선명하게
        self.ball.top = 500         # 핀 앞에 있던 공 다시 던지는 위치로 이동
        self.ball.rotate = 0        # 공 회전 각도 리셋
        self.ball.opacity = 1       # 핀에 공이 부딪혔을 때 사라진 공 다시 등장
        self.alive_pins = 10        # 핀 개수 재설정
        self.page.update()

    def update_scoreboard_ui(self):
        for i, frame in enumerate(self.all_frames_record):
            if i < 10:
                if i < 9: # 1-9프레임
                    if frame[0] == 10: self.score_cells[i].value = "X"
                    elif len(frame) == 2:
                        self.score_cells[i].value = "/" if sum(frame) == 10 else f"{frame[0]} {frame[1]}"
                    else: self.score_cells[i].value = str(frame[0])
                else: # 10프레임
                    res = []
                    for j, val in enumerate(frame):
                        if val == 10: res.append("X")
                        elif j > 0 and sum(frame[j-1:j+1]) == 10 and res[-1] != "X": res.append("/")
                        else: res.append(str(val))
                    self.score_cells[i].value = " ".join(res) # 프레임당 점수판 내 점수 동시 표시

        total = 0
        r_idx = 0 # 프레임 위치
        acc_scores = []
        for i in range(min(10, len(self.all_frames_record))):
            try:
                if i == 9:
                    total += sum(self.all_frames_record[9])
                    acc_scores.append(total)
                    break
                if self.only_rolls[r_idx] == 10:                # 스트라이크
                    total += 10 + self.only_rolls[r_idx+1] + self.only_rolls[r_idx+2]
                    r_idx += 1
                elif sum(self.only_rolls[r_idx:r_idx+2]) == 10: # 스페어
                    total += 10 + self.only_rolls[r_idx+2]
                    r_idx += 2
                else:                                           # 일반적인 상황
                    total += sum(self.only_rolls[r_idx:r_idx+2])
                    r_idx += 2
                acc_scores.append(total)
            except IndexError: 
            # 스트라이크, 스페어의 경우 다음 프레임에서 점수와 합산해야 하는데
            # 사용자가 공을 굴리지 않았기 때문에 다음 판의 점수가 없음.
            # 때문에 예외 처리를 설정하여 다음 투구가 이루어지도록 break를 걸어 다음 프레임으로 넘김
                break

        for i, score in enumerate(acc_scores):
            self.acc_cells[i].value = str(score) # 계산된 점수를 각 칸에 입력
        if acc_scores:
            self.total_score_text.value = str(acc_scores[-1]) # 마지막 누적 점수를 TOTAL에 표시
        self.page.update()

    async def restart_game_action(self, e):
        self.init_game_data() # 게임 종료 이후, 재시작을 위해 각 기록 리셋(변수 초기화)
        await self.reset_lane_visuals() # 비동기 활용
        for cell in self.score_cells + self.acc_cells: cell.value = "" # 점수판 초기화
        self.total_score_text.value = "0" # 최종점수 초기화
        self.restart_button.visible = False # 재시작 버튼 숨기기
        self.roll_button.disabled = False # 공 굴리기 버튼 활성화
        self.status_text.value = "새 게임 시작!"
        self.page.update()

if __name__ == "__main__":
    ft.run(BowlingGame)