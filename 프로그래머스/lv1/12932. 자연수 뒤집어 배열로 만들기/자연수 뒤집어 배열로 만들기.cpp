#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {    
    vector<int> answer;
    int _n = n;
    while(0 < n) {
        answer.push_back(n % 10);
        n /= 10;
    }
    return answer;
}