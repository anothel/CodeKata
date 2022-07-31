#include <string>
#include <vector>

using namespace std;

int gcd(const int &a, const int &b) {
  if (b == 0) {
    return a;
  } else {
    return gcd(b, a % b);
  }
}

int lcm(const int &a, const int &b) { return (a * b) / gcd(a, b); }

int solution(vector<int> arr) {
    int answer = arr[0];

    for(int i = 0; i < arr.size(); i++) {
        answer = lcm(answer, arr[i]);
    }
    
    return answer;
}