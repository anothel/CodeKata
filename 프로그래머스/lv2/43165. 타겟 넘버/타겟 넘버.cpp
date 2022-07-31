#include <string>
#include <vector>

using namespace std;

void dfs(const vector<int> &numbers, const int &target, const int &count, const int &sum, int &answer) {    
    if(numbers.size() == count) {
        if(sum == target) answer++;
        return;        
    } 
    
    dfs(numbers, target, count + 1, sum + numbers.at(count), answer);
    dfs(numbers, target, count + 1, sum - numbers.at(count), answer);
    
    return;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;  
    
    dfs(numbers, target, 0, 0, answer);
    
    return answer;
}