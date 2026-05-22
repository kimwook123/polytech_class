#include "product.h"
#include <iostream>

// 정적 데이터 멤버 클래스 외부 초기화
int Product::totalCount = 0;

Product::Product(std::string name, int price) : name(name)
{
    // 가격이 0보다 작을 수 없다는 불변 속성 검증
    if (price < 0)
    {
        this->price = 0;
    }
    else
    {
        this->price = price;
    }

    totalCount++; // 객체가 생성될 때마다 총 개수 1 증가
    std::cout << "제품 등록: " << this->name << std::endl;
}

Product::~Product()
{
    totalCount--; // 객체가 소멸될 때 총 개수 1 감소
}

// 정적 멤버 함수 구현
int Product::getTotalCount()
{
    return totalCount;
}