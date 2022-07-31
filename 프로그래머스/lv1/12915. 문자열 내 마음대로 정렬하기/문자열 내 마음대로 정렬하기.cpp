#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int index;
bool ssort(const string& s1, const string& s2) {
    if(s1[index] == s2[index]) {
        return s1 < s2;
    }
    return s1[index] < s2[index];
}

vector<string> solution(vector<string> strings, int n) {
    index = n;
    std::sort(strings.begin(), strings.end(), ssort);
    return strings;
}