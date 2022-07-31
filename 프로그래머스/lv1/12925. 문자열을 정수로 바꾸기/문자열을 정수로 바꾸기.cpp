#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int plus = 1;
    if(s.at(0) == '-') {
        s.erase(s.begin());
        plus *= -1;
    }
    
    return stoi(s) * plus;
}