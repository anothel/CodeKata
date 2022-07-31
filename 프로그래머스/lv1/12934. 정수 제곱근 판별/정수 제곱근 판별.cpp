#include <string>
#include <vector>
#include<cmath>

using namespace std;

long long solution(long long n) {
    long long answer = -1;
    
    for(int i = 0; i <= n; i++) {
        if(pow(i, 2) == n) {
            answer = pow(i + 1, 2);
            break;
        }
    }    
    
    return answer;
}