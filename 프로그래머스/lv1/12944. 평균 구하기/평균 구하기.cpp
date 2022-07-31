#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    for(auto x : arr) {
        answer += x;        
    }
    
    return answer / arr.size();
}