import market_total_library as m_t_l

def clear_screen():
    m_t_l.os.system('cls' if m_t_l.os.name == 'nt' else 'clear')

# 박스 디자인 출력 함수 (공통 사용)
def print_box(text, title=""):
    lines = text.strip().split('\n')
    width = max(len(line.encode('utf-8')) for line in lines) # 한글 인코딩 고려 너비 계산
    # 실제 터미널에서 한글 너비 조절을 위해 고정 폭 사용
    width = 50 
    
    print("\n" + "=" * width)
    if title:
        print(f"{title:^50}")
        print("-" * width)
    for line in lines:
        print(f" {line}")
    print("=" * width)

def get_visible_width(text):
    """한글은 2칸, 영문/숫자는 1칸으로 계산하여 실제 너비를 반환"""
    width = 0
    for char in text:
        if ord('가') <= ord(char) <= ord('힣'): # 한글 범위
            width += 2
        else:
            width += 1
    return width

def pad_text(text, target_width):
    """한글 너비를 고려하여 목표 너비만큼 공백을 채움"""
    current_width = get_visible_width(text)
    return text + ' ' * (target_width - current_width)

def print_item_table(item_list, col_count=5): # 가독성을 위해 열 개수를 5~6개로 조정 권장
    print("\n==================================================")
    print(f"{'ITEM MENU':^50}")
    print("--------------------------------------------------")
    print(" 판매 중인 물품 리스트")
    print("==================================================")
    
    # 한 칸의 너비를 12로 설정 (한글 5자 + 여유공백 2칸 정도)
    cell_width = 12 
    
    for i in range(0, len(item_list), col_count):
        row = item_list[i:i+col_count]
        # 각 아이템마다 너비를 계산해서 출력
        line = "".join(pad_text(item, cell_width) for item in row)
        print(line)
        
    print("==================================================")

def print_item_bucket(wishlist_cart, col_count=5): 
    cart_items = list(wishlist_cart.keys())
    
    print("\n==================================================")
    print(f"{'MY CART STATUS':^50}")
    print("--------------------------------------------------")
    print(" 내가 고른 물품 및 수량 리스트")
    print("==================================================")
    
    if not cart_items:
        print(" 장바구니가 비어 있습니다.")
    else:
        cell_width = 15 
        for i in range(0, len(cart_items), col_count):
            row = cart_items[i : i + col_count]
            
            # 물품명(개수) 형식으로 문자열을 만들어 pad_text에 전달합니다.
            line = "".join(pad_text(f"{item}({wishlist_cart[item]})", cell_width) for item in row)
            print(line)
        
    print("==================================================")