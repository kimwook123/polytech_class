#ifndef PRODUCT_H
#define PRODUCT_H

#include <string>

class Product
{
private:
    std::string name;
    int price;
    static int totalCount; // 모든 인스턴스가 공유하는 정적 데이터 멤버

public:
    Product(std::string name, int price); // 생성자
    ~Product();                           // 소멸자
    static int getTotalCount();           // 정적 멤버 함수
};

#endif