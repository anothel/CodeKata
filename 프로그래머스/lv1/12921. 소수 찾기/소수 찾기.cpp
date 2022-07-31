#include <string>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

bool table[1000000] = {false,};

int solution(int n) {
    int answer = 0;
    
    for(int i = 2; i <= n; i++ ) {
        if(table[i - 1] == true) continue;
        answer++;
        for(int j = i + i; j <= n; j+=i) {
            table[j - 1] = true;
        }
    }
    return answer;
}