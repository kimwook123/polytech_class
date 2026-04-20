import flet as ft
import random

def main(page: ft.Page):
    # 1. 페이지 초기 설정
    page.title = "Flet 업다운 게임"
    page.window_width = 400
    page.window_height = 550
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # 가로축 정렬을 중앙 정렬로 하였음
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 세로축 정렬 또한 중앙 정렬

    # 2. 게임에 필요한 상태 변수 (함수 안에 선언)
    # 정답 숫자와 시도 횟수를 초기화
    target_number = random.randint(1, 100)
    attempts = 0

    # 3. UI 요소 정의
    title = ft.Text(
        "숫자 맞추기 UP & DOWN", 
        size=30, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.BLUE_600
    )
    
    result_text = ft.Text(
        "1부터 100 사이의 숫자를 입력하세요!", 
        size=18, 
        color=ft.Colors.BLUE_GREY_700
    )
    
    input_field = ft.TextField(
        label="숫자 입력", 
        width=200, 
        text_align=ft.TextAlign.CENTER
    )

    # 4. 게임 로직 함수
    def check_guess(e):
        # 함수 밖에 있는 변수들을 수정하기 위해 nonlocal 선언
        nonlocal target_number, attempts
        
        try:
            val = int(input_field.value)
            attempts += 1

            if val < 1 or val > 100:
                result_text.value = "1~100 사이의 숫자만 가능합니다!"
                result_text.color = ft.Colors.RED_400
            elif val < target_number:
                result_text.value = f"({val}보다 큽니다)"
                result_text.color = ft.Colors.ORANGE_700
            elif val > target_number:
                result_text.value = f"({val}보다 작습니다)"
                result_text.color = ft.Colors.PURPLE_700
            else:
                result_text.value = f"정답입니다! 당신은 ({attempts}회만에 맞추셨습니다.)"
                result_text.color = ft.Colors.GREEN_700
                input_field.disabled = True
                submit_btn.visible = False
                reset_btn.visible = True
            
            input_field.value = ""
            input_field.focus()
            page.update()
            
        except ValueError:
            result_text.value = "숫자를 정확히 입력해 주세요!"
            result_text.color = ft.Colors.RED_400
            page.update()

    def reset_game(e):
        nonlocal target_number, attempts
        target_number = random.randint(1, 100)
        attempts = 0
        result_text.value = "1부터 100 사이의 숫자를 입력하세요!"
        result_text.color = ft.Colors.BLUE_GREY_700
        input_field.disabled = False
        input_field.value = ""
        submit_btn.visible = True
        reset_btn.visible = False
        page.update()

    # 5. 버튼 및 이벤트 연결
    input_field.on_submit = check_guess # 엔터 키 지원
    submit_btn = ft.ElevatedButton("확인", icon=ft.Icons.CHECK, on_click=check_guess)
    reset_btn = ft.FilledButton("다시 시작하기", icon=ft.Icons.REPLAY, on_click=reset_game, visible=False)

    # 6. 화면에 배치
    page.add(
        # 인자들을 세로로 나열해서 가독성을 높임
        ft.Column(
            [
                title,
                ft.Divider(height=20, color="transparent"), # 구분선을 투명 선으로 그었음
                result_text,
                ft.Container(height=20), # 구성 요소들 간에 간격을 넣음
                input_field,
                submit_btn,
                reset_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# 실행
if __name__ == "__main__":
    ft.app(target=main) 
    """
    Flet 어플을 실행하기 위한 함수
    app 함수 내 target 인자는 앱의 시작점을 지칭(==main)
    """