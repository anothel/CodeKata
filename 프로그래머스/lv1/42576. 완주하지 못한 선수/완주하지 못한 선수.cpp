#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
  string answer = "";
  map<string, int> table;

  for (auto x : completion) {
    table[x]++;
  }

  for (auto x : participant) {
    if (--table[x] < 0) {
      answer = x;
      break;
    } else {
      continue;
    }
  }

  return answer;
}