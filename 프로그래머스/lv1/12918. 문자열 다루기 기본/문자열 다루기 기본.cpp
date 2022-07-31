#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    if(s.length() != 4 && s.length() != 6) return false;
    for(auto x : s) if(x < '0' || '9' < x) return false;
    return true;
}