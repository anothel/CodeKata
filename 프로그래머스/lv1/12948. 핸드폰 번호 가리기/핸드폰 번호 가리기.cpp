#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = "";
    for(int i = 0; i < phone_number.length(); i++) {
        if(4 < phone_number.length() - i) {
            answer += "*";
        } else {
            answer += phone_number.at(i);
        }        
    }
    return answer;
}