#include <iostream>
#include <bitset>  // 16진수와 2진수를 나타내기 위한 헤더파일 추가
#include <limits>  // 오버플로우/언더플로우 체크를 위해 헤더파일 추가
#include <cstring> // 문자열 처리

using namespace std;
// 4개의 사칙연산 중 오버플로우/언더플로우 방지를 위한 함수
bool calculateSafe(long long current, int next, char op, long long &result)
{                          // current = 중간결과, next = 다음 숫자, op = 연산자, &result = 결과 저장
    long long temp_result; // result에 중간중간 넘기지 않고 최종결과만 전달 목적
    if (op == '+')
        temp_result = current + next;
    else if (op == '-')
        temp_result = current - next;
    else if (op == '*')
        temp_result = current * next;
    else if (op == '/')
    {
        if (next == 0)
            return false;
        if (current == numeric_limits<int>::min() && next == -1)
            return false; // 나누는 수가 -1일 때의 오버플로우 체크
        temp_result = current / next;
    }
    else
        return false; // 사용자가 사칙연산 이외의 연산자를 입력한 경우

    if (temp_result > numeric_limits<int>::max() ||
        temp_result < numeric_limits<int>::min())
        return false; // 결과가 int 범위를 벗어나는 경우

    result = temp_result;
    return true;
}

int main()
{
    int numbers[4];    // 입력받은 4개 숫자 저장 배열
    char operators[3]; // 입력받은 3개 연산자 저장 배열

    for (int i = 0; i < 3; i++)
    {
        cout << i + 1 << "번째 숫자를 입력하시오";
        cin >> numbers[i];

        cout << i + 1 << "번째 연산자를 입력하시오(사칙연산 + - * /만 입력)";
        cin >> operators[i];
    }
    cout << "4번째 숫자를 입력하시오";
    cin >> numbers[3];

    // 우선순위 계산 (곱셈, 나눗셈)
    for (int i = 0; i < 3; i++)
    {
        if (operators[i] == '*' || operators[i] == '/')
        {
            long long temp;
            // long long으로 중간 결과를 저장하여 오버플로우 방지

            if (!calculateSafe(numbers[i], (int)numbers[i + 1], operators[i], temp))
            {
                cout << "오버플로우 발생!" << endl;
                return 1;
            }
            numbers[i] = temp;  // 앞의 숫자를 결과로 교체
            numbers[i + 1] = 0; // 뒤의 숫자는 비움 (더하기 연산에 영향 없게)
            operators[i] = '+'; // 연산자는 +로 변경
        }
    }

    // 우선순위 계산 (덧셈, 뺄셈)
    long long final_res = numbers[0];
    for (int i = 0; i < 3; i++)
    {
        if (!calculateSafe(final_res, (int)numbers[i + 1], operators[i], final_res))
        {
            cout << "오버플로우 발생!" << endl;
            return 1;
        }
    }

    // 4. 결과 출력
    cout << "\n[ 결과 ]" << endl;
    // int형 결과를 32비트 2진수 문자열로 변환
    string bin_str = bitset<32>(final_res).to_string();
    cout << "Bin : " << bin_str.substr(bin_str.find('1')) << endl; // 첫 '1'부터 출력
    cout << "Dec : " << dec << final_res << endl;
    cout << "Hex : 0x" << hex << uppercase << final_res << endl;

    return 0;
Error:
    cout << "계산 중 오류가 발생했습니다." << endl;
    return 1;
}