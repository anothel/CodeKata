#include <string>
#include <vector>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    bool odd = true;
    for(int i = left; i <= right; i++) {
        odd = true;
        for(int j = 1; j <= i; j++) {
            if(j * j == i) {
                odd = false;
                break;
            }
        }
        answer = odd ? answer + i : answer - i;
    }
    
    return answer;
}