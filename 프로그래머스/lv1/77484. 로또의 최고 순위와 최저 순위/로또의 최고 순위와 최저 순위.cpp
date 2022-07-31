#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    map<int, int> table = {{6, 1}, {5, 2}, {4, 3}, {3, 4,}, {2, 5}, {1, 6}, {0, 6}};
    
    int count = 0, zeroCount = 0;
    
    for(auto x : lottos) {
        if(x == 0) zeroCount++;
        for(auto y : win_nums) {
            if(x == y) {
                count++;
            }
        }
    }
    answer.push_back(table[count + zeroCount]);
    answer.push_back(table[count]);
    
    return answer;
}