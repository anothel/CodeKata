#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer(arr);
    
    int min = answer.at(0);
    int at = 0;
    
    for(int i = 0; i < answer.size(); i++) {
        if(answer.at(i) < min) {
            min = answer.at(i);
            at = i;
        }        
    }
    
    answer.erase(answer.begin() + at);
    
    if(answer.empty() == true) answer.push_back(-1);
    
    return answer;
}