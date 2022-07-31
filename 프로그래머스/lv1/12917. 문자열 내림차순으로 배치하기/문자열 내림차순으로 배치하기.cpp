#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    std::sort(s.begin(), s.end());
    std::reverse(s.begin(), s.end());
    return s;
}