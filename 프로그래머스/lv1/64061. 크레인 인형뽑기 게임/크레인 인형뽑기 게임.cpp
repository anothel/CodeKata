#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> table;
    
    for(int move : moves) {
        for(vector<int>& x : board) {
            int& doll = x.at(move - 1);
            if (doll == 0) {
                continue;
            }
            if(!table.empty() && table.back() == doll) {
                answer += 2;
                table.pop_back();
            } else {
                table.push_back(doll);
            }
            doll = 0;
            break;
        }
    }

    return answer;
}