using namespace std;

long long solution(int price, int money, int count)
{
    long long value = 0;
    for(int i = 1; i <= count; i++) {
        value += price * i;        
    }

    return money < value ? value - money : 0;
}