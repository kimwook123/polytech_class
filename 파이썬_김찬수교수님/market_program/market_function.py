import design as ds
import market_total_library as m_t_l

# 총매출, 판매 아이템 가격 및 재고 함수
def database_input(item_list):
    today_total_sales = 0
    item_payment = {}
    item_DB = {}
    for i in item_list:
        item_payment[i] = m_t_l.random.randrange(1000, 10000, 100)
        item_DB[i] = m_t_l.random.randint(1, 10)
    return item_payment, item_DB, today_total_sales

# 관리자 - 아이템 관련 작업 함수
def Item_Inventory_check(item_DB, item_list):
    ds.clear_screen()
    print(item_list)
    print("===========작업 목록===========\n")
    print("1. 재고 확인\n")
    print("2. 재고 변경\n")
    choose = int(input(""))
    if choose == 1:
        storage_check_option(item_DB, item_list)
    elif choose == 2:
        storage_change_option(item_DB, item_list)
    else:
        print("올바른 선택지를 골라주세요.")
        m_t_l.time.sleep(0.5)

# 관리자 - 재고 확인 함수
def storage_check_option(item_DB, item_list):
    while True:
            ds.clear_screen()
            print(item_list)
            checking_item = input("재고를 확인할 물품을 입력하세요.\n")
            if checking_item not in item_DB:
                print("해당 제품은 저희 매장에 없는 제품입니다.")
            else:
                item_count = item_DB[checking_item]
                print(f"{checking_item} 은 현재 {item_count} 개 있습니다.")

            more_check = input("더 검색하십니까(예:1, 종료:2): \n")
            if more_check == '2':
                break
            elif more_check == '1':
                pass
            else:
                print("올바른 선택지를 골라주세요.")

# 관리자 - 재고 변경 함수
def storage_change_option(item_DB, item_list):
    while True:
        ds.clear_screen()
        print(item_list)
        print("===========작업 목록===========\n")
        print("1. 재고 추가\n")
        print("2. 재고 삭제\n")
        print("3. 뒤로가기\n")
        storage_change = input("작업을 선택하세요.\n")
        if storage_change == '1':
            wish_change_item = input("재고 변경 물품: ")
            item_change_count = int(input("몇 개를 추가하시겠습니까?: "))
            item_DB[wish_change_item] += item_change_count
            print(f"{wish_change_item}의 재고가 {item_change_count}개 추가되었습니다.")
            m_t_l.time.sleep(0.5)
        elif storage_change == '2':
            wish_change_item = input("재고 변경 물품: ")
            item_change_count = int(input("몇 개를 삭제하시겠습니까?: "))
            item_DB[wish_change_item] -= item_change_count
            print(f"{wish_change_item}의 재고가 {item_change_count}개 삭제되었습니다.")
            m_t_l.time.sleep(0.5)
        elif storage_change == '3':
            break
        else:
            print("올바른 선택지를 골라주세요.")
            m_t_l.time.sleep(0.5)


# 사용자 선택 함수
def market_user_contact():
    ds.clear_screen()
    menu_text = "1. 물품 구매\n2. 관리자 메뉴"
    ds.print_box(menu_text, title="인지소 매점 방문")
    who_user = input("번호를 선택해 주세요: ")
    return who_user

# 고객이 장바구니에 물품을 담는 함수
def wishlist_collect(item_payment ,item_DB, item_list):
    wishlist_cart = {}
    while True:
        ds.print_item_table(item_list)
        ds.print_item_bucket(wishlist_cart)
        wishlist = input("\n구매할 물품 입력 (그만 고르기: -1): ")
        
        if wishlist == "-1":
            break
        elif wishlist not in item_list:
            ds.print_box("해당 물품은 판매하지 않습니다.")
            m_t_l.time.sleep(2)
            continue

        item_inventory = item_DB[wishlist]
        status_text = f"상품명: {wishlist}\n가격: {item_payment[wishlist]}원\n현재 재고: {item_inventory}개"
        ds.print_box(status_text, title="상품 정보")

        if item_inventory == 0:
            ds.print_box("해당 물품은 매진되었습니다.")
            m_t_l.time.sleep(2)
            continue

        try:
            wishlist_count = int(input("구매 수량을 입력하세요: "))
            if wishlist_count > item_inventory:
                ds.print_box("재고가 부족합니다! 더 적은 수량을 입력해 주세요.")
                m_t_l.time.sleep(1)
            elif wishlist_count <= 0:
                ds.print_box("1개 이상의 수량을 입력해 주세요.")
                m_t_l.time.sleep(1)
            else:
                wishlist_cart[wishlist] = wishlist_cart.get(wishlist, 0) + wishlist_count
                item_DB[wishlist] -= wishlist_count
                ds.print_box(f"{wishlist} {wishlist_count}개가 장바구니에 담겼습니다.")
                m_t_l.time.sleep(2)
        except ValueError:
            ds.print_box("숫자만 입력 가능합니다.")
            m_t_l.time.sleep(1)
            
    return wishlist_cart

# 결제 함수
def end_pay(wishlist_cart, item_payment, today_total_sales):
    if not wishlist_cart:
        ds.print_box("구매 내역이 없어 결제를 종료합니다.")
        m_t_l.time.sleep(2)
        return today_total_sales

    receipt = ""
    total_pay = 0
    for name, count in wishlist_cart.items():
        sub_total = count * item_payment[name]
        total_pay += sub_total
        receipt += f"{name}: {count}개 x {item_payment[name]}원 = {sub_total}원\n"

    receipt += f"\n총 결제 금액: {total_pay}원"
    ds.print_box(receipt, title="영 수 증")

    while True:
        payment_menu = input("결제 수단 (카드, 현금, 삼성페이): ")
        if payment_menu in ['카드', '현금', '삼성페이']:
            break
        print("정확한 결제 방식을 선택해 주세요.")
    
    ds.print_box("결제가 완료되었습니다! 감사합니다.", title="결제 완료")
    m_t_l.time.sleep(2)
    return today_total_sales + total_pay

# market_function.py 내부에 추가
def run_market_system(itemlist, item_payment, item_DB, today_total_sales):
    """매점 시스템의 메인 루프를 관리하는 함수"""
    while True:
        who = market_user_contact()  # 사용자 선택창
        
        if who == '2':  # 관리자 모드
            Item_Inventory_check(item_DB, itemlist)
            continue
            
        elif who == '1':  # 구매 모드
            # ds는 design 모듈이므로, market_function 내에서 호출하려면 
            # 해당 파일 상단에 import design as ds가 되어 있어야 함
            wishlistcart = wishlist_collect(item_payment, item_DB, itemlist)
            today_total_sales = end_pay(wishlistcart, item_payment, today_total_sales)
            
        else:
            import design as ds # 혹은 파일 상단에 import
            ds.print_box("잘못된 입력입니다.")
            continue

        # 루프 유지 여부 확인
        re_order = input("\n계속 쇼핑하시겠습니까? (계속: 아무키, 나가기: -1): ")
        if re_order == "-1":
            import design as ds
            ds.clear_screen()
            ds.print_box(f"오늘의 총 매출액: {today_total_sales}원", title="영업 종료")
            break
            
    return today_total_sales # 필요 시 최종 매출액 반환

