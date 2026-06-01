#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LineEditor:
    """라인 편집기 - 간단한 텍스트 파일 편집 도구"""
    
    def __init__(self):
        self.lines = []
    
    def insert(self, line_num, text):
        """i: 라인 삽입"""
        try:
            line_num = int(line_num)
            if line_num < 0 or line_num > len(self.lines):
                print(f"오류: 유효하지 않은 행 번호 {line_num}")
                return False
            self.lines.insert(line_num, text)
            print(f"행 {line_num}에 '{text}'를 삽입했습니다.")
            return True
        except ValueError:
            print("오류: 행 번호는 정수여야 합니다.")
            return False
    
    def delete(self, line_num):
        """d: 한 라인 삭제"""
        try:
            line_num = int(line_num)
            if line_num < 0 or line_num >= len(self.lines):
                print(f"오류: 유효하지 않은 행 번호 {line_num}")
                return False
            deleted_text = self.lines.pop(line_num)
            print(f"행 {line_num}을 삭제했습니다: '{deleted_text}'")
            return True
        except ValueError:
            print("오류: 행 번호는 정수여야 합니다.")
            return False
    
    def replace(self, line_num, text):
        """r: 한 라인 변경"""
        try:
            line_num = int(line_num)
            if line_num < 0 or line_num >= len(self.lines):
                print(f"오류: 유효하지 않은 행 번호 {line_num}")
                return False
            old_text = self.lines[line_num]
            self.lines[line_num] = text
            print(f"행 {line_num}을 변경했습니다.")
            print(f"  이전: '{old_text}'")
            print(f"  변경: '{text}'")
            return True
        except ValueError:
            print("오류: 행 번호는 정수여야 합니다.")
            return False
    
    def print_content(self):
        """p: 현재 내용 출력"""
        if not self.lines:
            print("(문서가 비어있습니다)")
            return
        
        print("\n--- 현재 문서 ---")
        for i, line in enumerate(self.lines):
            print(f"{i}: {line}")
        print(f"--- 총 {len(self.lines)}줄 ---\n")
    
    def load_file(self, filename):
        """l: 파일 입력"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.lines = [line.rstrip('\n') for line in f.readlines()]
            print(f"파일 '{filename}'에서 {len(self.lines)}줄을 읽었습니다.")
            return True
        except FileNotFoundError:
            print(f"오류: 파일 '{filename}'을 찾을 수 없습니다.")
            return False
        except Exception as e:
            print(f"오류: 파일을 읽는 중 오류가 발생했습니다: {e}")
            return False
    
    def save_file(self, filename):
        """s: 파일 출력"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for line in self.lines:
                    f.write(line + '\n')
            print(f"파일 '{filename}'에 {len(self.lines)}줄을 저장했습니다.")
            return True
        except Exception as e:
            print(f"오류: 파일을 저장하는 중 오류가 발생했습니다: {e}")
            return False
    
    def show_help(self):
        """도움말 표시"""
        print("\n--- 라인 편집기 명령어 ---")
        print("i <행번호> <텍스트>  : 라인 삽입")
        print("d <행번호>           : 라인 삭제")
        print("r <행번호> <텍스트>  : 라인 변경")
        print("p                    : 현재 내용 출력")
        print("l <파일명>           : 파일 입력 (기본값: test.txt)")
        print("s <파일명>           : 파일 출력 (기본값: test.txt)")
        print("h                    : 도움말")
        print("q                    : 편집기 종료")
        print("--- 라인 편집기 ---\n")
    
    def run(self):
        """편집기 실행"""
        self.show_help()
        
        while True:
            try:
                user_input = input("편집기> ").strip()
                
                if not user_input:
                    continue
                
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()
                
                if command == 'q':
                    print("편집기를 종료합니다.")
                    break
                
                elif command == 'p':
                    self.print_content()
                
                elif command == 'h':
                    self.show_help()
                
                elif command == 'i':
                    if len(parts) < 2:
                        print("오류: i 명령은 '행번호 텍스트' 형태로 입력하세요.")
                        continue
                    args = parts[1].split(maxsplit=1)
                    if len(args) < 2:
                        print("오류: i 명령은 '행번호 텍스트' 형태로 입력하세요.")
                        continue
                    self.insert(args[0], args[1])
                
                elif command == 'd':
                    if len(parts) < 2:
                        print("오류: d 명령은 '행번호' 형태로 입력하세요.")
                        continue
                    self.delete(parts[1])
                
                elif command == 'r':
                    if len(parts) < 2:
                        print("오류: r 명령은 '행번호 텍스트' 형태로 입력하세요.")
                        continue
                    args = parts[1].split(maxsplit=1)
                    if len(args) < 2:
                        print("오류: r 명령은 '행번호 텍스트' 형태로 입력하세요.")
                        continue
                    self.replace(args[0], args[1])
                
                elif command == 'l':
                    filename = parts[1] if len(parts) > 1 else 'test.txt'
                    self.load_file(filename)
                
                elif command == 's':
                    filename = parts[1] if len(parts) > 1 else 'test.txt'
                    self.save_file(filename)
                
                else:
                    print(f"오류: 알 수 없는 명령 '{command}'. 'h'를 입력해 도움말을 보세요.")
            
            except KeyboardInterrupt:
                print("\n편집기를 종료합니다.")
                break
            except Exception as e:
                print(f"오류: {e}")


if __name__ == '__main__':
    editor = LineEditor()
    editor.run()
