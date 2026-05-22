#include <iostream>
#include "product.h"

int main()
{
    // 첫 번째 객체 생성
    Product p1("노트북", 1500000);

    // 클래스 이름(Product::)을 통해 정적 함수 호출
    std::cout << "현재 총 제품 수: " << Product::getTotalCount() << std::endl;

    // 인위적인 블록을 생성하여 객체 생명 주기 제한
    {
        std::cout << "--- 블록 진입 ---" << std::endl;
        Product p2("마우스", 50000);
        std::cout << "현재 총 제품 수: " << Product::getTotalCount() << std::endl;
    } // <-- 이 블록을 빠져나가는 순간 p2의 소멸자가 자동으로 호출됨

    std::cout << "--- 블록 탈출 (소멸자 호출됨) ---" << std::endl;
    std::cout << "현재 총 제품 수: " << Product::getTotalCount() << std::endl;

    return 0;
}