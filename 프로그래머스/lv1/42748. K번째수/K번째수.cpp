#include <string>
#include <vector>

#include <algorithm>

using namespace std;

int getNumber(const vector<int> &array, const vector<int> &commands) {
    vector<int> contents;
    
    for(int i = commands.at(0); i <= commands.at(1); i++) {
        contents.push_back(array.at(i-1));
    }
    
    sort(contents.begin(), contents.end());    
    
    return contents.at(commands.at(2) - 1 );
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(auto x : commands) {
        answer.push_back(getNumber(array, x));
    }
    
    return answer;
}