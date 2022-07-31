#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

bool isSosoo(int n) {
  bool result = true;
  for (int i = 2; i <= sqrt(n); i++) {
    if (n % i == 0) {
      result = false;
    }
  }
  return result;
}

int solution(vector<int> nums) {
  int answer = 0;
  sort(nums.begin(), nums.end());
  for (int i = 0; i < nums.size() - 2; i++)
    for (int j = i + 1; j < nums.size() - 1; j++)
      for (int k = j + 1; k < nums.size(); k++) {
        int sum = nums[i] + nums[j] + nums[k];
        if (isSosoo(sum)) answer++;
      }
  return answer;
}