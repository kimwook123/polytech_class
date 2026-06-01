import flet as ft


class LineEditorUI:
    def __init__(self):
        self.lines = []
        self.current_file = "test.txt"
    
    def build_ui(self, page: ft.Page):
        page.title = "라인 편집기"
        page.window_width = 900
        page.window_height = 700
        page.padding = 20
        
        # 타이틀
        title = ft.Text(
            "라인 편집기",
            size=28,
            weight="bold",
            color="#333"
        )
        
        # 파일명 입력
        self.file_input = ft.TextField(
            label="파일명",
            value="test.txt",
            width=300,
        )
        
        # 파일명 업데이트 함수
        def update_filename(e):
            self.current_file = self.file_input.value or "test.txt"
            self.update_status(f"파일명: {self.current_file}")
        
        self.file_input.on_change = update_filename
        
        # 콘텐츠 출력 영역
        self.content_display = ft.Text(
            value="(문서가 비어있습니다)",
            size=12,
            color="#333"
        )
        
        # 스크롤 컨테이너
        content_container = ft.Container(
            content=self.content_display,
            bgcolor="#f5f5f5",
            border_radius=8,
            padding=15,
            height=300,
            expand=True,
        )
        
        # 라인 번호 입력
        self.line_num_input = ft.TextField(
            label="행 번호",
            width=100,
        )
        
        # 텍스트 입력
        self.text_input = ft.TextField(
            label="텍스트",
            expand=True,
        )
        
        # 버튼들
        def on_insert(e):
            try:
                line_num = int(self.line_num_input.value) if self.line_num_input.value else -1
                text = self.text_input.value
                
                if line_num < 0 or line_num > len(self.lines):
                    self.update_status(f"오류: 유효하지 않은 행 번호 {line_num}")
                    return
                
                self.lines.insert(line_num, text)
                self.update_status(f"행 {line_num}에 '{text}'를 삽입했습니다.")
                self.line_num_input.value = ""
                self.text_input.value = ""
                self.refresh_content()
            except ValueError:
                self.update_status("오류: 행 번호는 정수여야 합니다.")
        
        def on_delete(e):
            try:
                line_num = int(self.line_num_input.value)
                
                if line_num < 0 or line_num >= len(self.lines):
                    self.update_status(f"오류: 유효하지 않은 행 번호 {line_num}")
                    return
                
                deleted_text = self.lines.pop(line_num)
                self.update_status(f"행 {line_num}을 삭제했습니다: '{deleted_text}'")
                self.line_num_input.value = ""
                self.refresh_content()
            except ValueError:
                self.update_status("오류: 행 번호는 정수여야 합니다.")
        
        def on_replace(e):
            try:
                line_num = int(self.line_num_input.value)
                text = self.text_input.value
                
                if line_num < 0 or line_num >= len(self.lines):
                    self.update_status(f"오류: 유효하지 않은 행 번호 {line_num}")
                    return
                
                old_text = self.lines[line_num]
                self.lines[line_num] = text
                self.update_status(f"행 {line_num}을 변경했습니다.")
                self.line_num_input.value = ""
                self.text_input.value = ""
                self.refresh_content()
            except ValueError:
                self.update_status("오류: 행 번호는 정수여야 합니다.")
        
        def on_load(e):
            try:
                filename = self.current_file
                with open(filename, 'r', encoding='utf-8') as f:
                    self.lines = [line.rstrip('\n') for line in f.readlines()]
                self.update_status(f"파일 '{filename}'에서 {len(self.lines)}줄을 읽었습니다.")
                self.refresh_content()
            except FileNotFoundError:
                self.update_status(f"오류: 파일 '{self.current_file}'을 찾을 수 없습니다.")
            except Exception as ex:
                self.update_status(f"오류: {ex}")
        
        def on_save(e):
            try:
                filename = self.current_file
                with open(filename, 'w', encoding='utf-8') as f:
                    for line in self.lines:
                        f.write(line + '\n')
                self.update_status(f"파일 '{filename}'에 {len(self.lines)}줄을 저장했습니다.")
            except Exception as ex:
                self.update_status(f"오류: {ex}")
        
        def on_clear(e):
            self.lines = []
            self.update_status("문서가 초기화되었습니다.")
            self.refresh_content()
        
        # 버튼들
        insert_btn = ft.Button(
            "삽입 (i)",
            on_click=on_insert,
            bgcolor="#007AFF",
            color="white",
            height=40,
        )
        
        delete_btn = ft.Button(
            "삭제 (d)",
            on_click=on_delete,
            bgcolor="#007AFF",
            color="white",
            height=40,
        )
        
        replace_btn = ft.Button(
            "변경 (r)",
            on_click=on_replace,
            bgcolor="#007AFF",
            color="white",
            height=40,
        )
        
        load_btn = ft.Button(
            "파일 읽기 (l)",
            on_click=on_load,
            bgcolor="#34C759",
            color="white",
            height=40,
        )
        
        save_btn = ft.Button(
            "파일 저장 (s)",
            on_click=on_save,
            bgcolor="#34C759",
            color="white",
            height=40,
        )
        
        clear_btn = ft.Button(
            "초기화",
            on_click=on_clear,
            bgcolor="#FF3B30",
            color="white",
            height=40,
        )
        
        # 상태 표시 바
        self.status_bar = ft.Text(
            value="준비됨",
            size=11,
            color="#666"
        )
        
        status_container = ft.Container(
            content=self.status_bar,
            bgcolor="#f0f0f0",
            border_radius=6,
            padding=10,
        )
        
        # 레이아웃 구성
        page.add(
            # 제목
            title,
            
            # 파일명
            ft.Row(
                [ft.Text("파일명:", weight="bold"), self.file_input],
                spacing=10,
            ),
            
            # 콘텐츠 출력 영역
            ft.Text("현재 문서:", weight="bold", size=14),
            content_container,
            
            # 상태 바
            status_container,
            
            ft.Divider(),
            
            # 입력 섹션
            ft.Text("편집 도구:", weight="bold", size=14),
            
            ft.Row(
                [
                    self.line_num_input,
                    self.text_input,
                ],
                spacing=10,
                expand=True,
            ),
            
            # 버튼 행 1
            ft.Row(
                [insert_btn, delete_btn, replace_btn],
                spacing=10,
            ),
            
            # 버튼 행 2
            ft.Row(
                [load_btn, save_btn, clear_btn],
                spacing=10,
            ),
        )
    
    def refresh_content(self):
        """콘텐츠 새로 고침"""
        if not self.lines:
            self.content_display.value = "(문서가 비어있습니다)"
        else:
            content = "\n".join([f"{i}: {line}" for i, line in enumerate(self.lines)])
            self.content_display.value = content
        self.content_display.update()
    
    def update_status(self, message: str):
        """상태 메시지 업데이트"""
        self.status_bar.value = message
        self.status_bar.update()


def main(page: ft.Page):
    editor = LineEditorUI()
    editor.build_ui(page)


if __name__ == "__main__":
    ft.app(main)
