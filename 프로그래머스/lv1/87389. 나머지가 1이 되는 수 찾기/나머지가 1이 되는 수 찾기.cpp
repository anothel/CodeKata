#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    
            int i;
        for(i = 2; i <= n-1; i++) {
            if(n % i == 1) break;
        }        
        return i;
}