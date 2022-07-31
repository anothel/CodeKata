#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    
    for(auto x : arr) {
        if(answer.empty() == false && answer.back() == x) {
            continue;
        }
        answer.push_back(x);
    }

    return answer;
}