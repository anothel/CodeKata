#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int result = 0;
    vector<int> v;
    while(n) {
        v.push_back(n % 3);
        n /= 3;
    }
    for(int i = v.size() - 1, j = 0; 0 <= i; i--, j++) {
        result += v.at(i) * pow(3, j);
    }
    
    return result;
}