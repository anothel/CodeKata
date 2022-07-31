#include <string>
#include <vector>

#include <iostream>

using namespace std;
bool isUpper(char c) {
    return ('A' <= c && c <= 'Z') ? true : false;
}

bool isLower(char c) {
    return ('a' <= c && c <= 'z') ? true : false;
}

bool isAlphabet(char c) {
  return isUpper(c) || isLower(c) ? true : false;
}

string solution(string s, int n) {
  string answer = "";
  bool bUpper = false;
  for (auto x : s) {
    if (x != ' ') {
        if(isUpper(x) == true) {
            x = (x - 65 + n) % 26;
            x += 65;
        } else {
            x = (x - 97 + n) % 26;
            x += 97;
        }

    } else {
        // Do nothing
    }
    answer += x;
  }
  return answer;
}