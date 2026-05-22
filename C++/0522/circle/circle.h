#ifndef CIRCLE_H
#define CIRCLE_H
#include <iostream>
#include <cassert>
using namespace std;
// 클래스 정의
class Circle
{
private:
    double radius;

public:
    Circle(double radius);         // 매개변수가 있는 생성자
    Circle();                      // 기본 생성자
    Circle(const Circle &circle);  // 복사 생성자
    ~Circle();                     // 소멸자
    void setRadius(double radius); // 설정자
    double getRadius() const;      // 접근자
    double getArea() const;        // 접근자
    double getPerimeter() const;   // 접근자
};
#endif