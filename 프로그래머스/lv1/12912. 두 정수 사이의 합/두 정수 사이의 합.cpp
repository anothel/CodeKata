#include <string>
#include <vector>

using namespace std;

long long solution(const int a, const int b) {
  long long answer = 0;

  for (int i = ((b <= a ? b : a)); i <= (a <= b ? b : a); i++) {
    answer += i;
  }
  return answer;
}