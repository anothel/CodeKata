#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    for(auto x : arr) {
        if (x % divisor == 0) {
            answer.push_back(x);
        }
    }
    sort(answer.begin(), answer.end());
    if(answer.size() == 0) {
        answer.push_back(-1);
    }
    return answer;
}