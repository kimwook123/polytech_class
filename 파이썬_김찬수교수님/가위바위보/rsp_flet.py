import flet as ft
import random

def main(page: ft.Page):
    # 페이지 설정
    page.title = "Flet 5판 3선승 가위바위보"
    page.window_width = 450
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # 게임 상태 변수
    user_score = 0
    com_score = 0
    game_over = False  # 게임 종료 여부 플래그
    options = ["가위", "바위", "보"]
    icons = {"가위": "✌️", "바위": "✊", "보": "🖐️"}

    # UI 요소 정의
    title = ft.Text("가위 바위 보!", size=30, weight="bold", color="blue700")
    score_display = ft.Text("나: 0  VS  컴퓨터: 0", size=25, weight="w500")
    result_text = ft.Text("가위, 바위, 보 중 하나를 선택하세요!", size=18, text_align="center")
    
    # 게임 로직 함수
    def play(user_choice):
        nonlocal user_score, com_score, game_over
        
        if game_over: return  # 게임이 이미 끝났으면 실행 안 함

        com_choice = random.choice(options)
        
        # 승패 판정
        if user_choice == com_choice:
            res_msg = "비겼습니다!"
        elif (user_choice == "가위" and com_choice == "보") or \
             (user_choice == "바위" and com_choice == "가위") or \
             (user_choice == "보" and com_choice == "바위"):
            res_msg = "이겼습니다! 🎉"
            user_score += 1
        else:
            res_msg = "졌습니다... 😢"
            com_score += 1

        # 화면 업데이트
        result_text.value = f"나: {icons[user_choice]}  VS  컴퓨터: {icons[com_choice]}\n{res_msg}"
        score_display.value = f"나: {user_score}  VS  컴퓨터: {com_score}"
        
        if user_score == 3:
            result_text.value = "🎊 축하합니다! 최종 승리하셨습니다! 🎊"
            result_text.color = "blue"
            game_over = True
            disable_buttons()
        elif com_score == 3:
            result_text.value = "💀 아쉽네요... 컴퓨터가 최종 승리했습니다."
            result_text.color = "red"
            game_over = True
            disable_buttons()
            
        page.update()

    # 버튼 비활성화 함수
    def disable_buttons():
        for btn in buttons_row.controls:
            btn.disabled = True
        reset_button.visible = True

    # 게임 리셋 함수
    def reset_game(e):
        nonlocal user_score, com_score, game_over
        user_score = 0
        com_score = 0
        game_over = False
        score_display.value = "나: 0  VS  컴퓨터: 0"
        result_text.value = "게임을 다시 시작합니다!"
        result_text.color = "black"
        for btn in buttons_row.controls:
            btn.disabled = False
        reset_button.visible = False
        page.update()

    # UI
    buttons_row = ft.Row(
        [
            ft.ElevatedButton("가위 ✌️", on_click=lambda _: play("가위"), width=110),
            ft.ElevatedButton("바위 ✊", on_click=lambda _: play("바위"), width=110),
            ft.ElevatedButton("보 🖐️", on_click=lambda _: play("보"), width=110),
        ],
        alignment="center"
    )

    reset_button = ft.ElevatedButton("다시 시작하기", on_click=reset_game, visible=False, color="white", bgcolor="blue")

    # 결과창 컨테이너
    result_container = ft.Container(
        content=result_text,
        padding=20,
        bgcolor="#f5f5f5",
        border_radius=15,
        alignment=ft.alignment.center,
        width=350,
        height=150,
    )

    page.add(
        title,
        ft.Divider(height=30, color="transparent"),
        score_display,
        ft.Divider(height=10, color="transparent"),
        result_container,
        ft.Divider(height=20, color="transparent"),
        buttons_row,
        ft.Divider(height=10, color="transparent"),
        reset_button
    )

if __name__ == "__main__":
    ft.app(target=main)