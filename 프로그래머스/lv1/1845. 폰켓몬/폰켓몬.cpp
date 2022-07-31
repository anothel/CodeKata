#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
    int answer = 0, count(nums.size() / 2);
    
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    
    return count < nums.size() ? count : nums.size();
}