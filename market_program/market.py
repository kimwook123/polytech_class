import item_library as i_lib
import market_function as m_func

# 메인 함수
def main():
    itemlist = i_lib.itemlist_menu()
    item_payment, item_DB, today_total_sales = m_func.database_input(itemlist)

    m_func.run_market_system(itemlist, item_payment, item_DB, today_total_sales)

if __name__ == "__main__":
    main()