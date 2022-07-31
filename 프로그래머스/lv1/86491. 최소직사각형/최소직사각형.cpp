#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_ver = 0, max_hor = 0;
    for(auto x : sizes) {
        if(x[0] < x[1]) {
            if(max_ver < x[1]) {
                max_ver = x[1];                
            }
            if(max_hor < x[0]) {
                max_hor = x[0];                
            }
        } else {
            if(max_ver < x[0]) {
                max_ver = x[0];                
            }
            if(max_hor < x[1]) {
                max_hor = x[1];                
            }
        }
    }
    return max_ver * max_hor;
}