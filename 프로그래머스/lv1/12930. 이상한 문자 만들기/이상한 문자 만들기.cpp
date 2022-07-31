#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool bCapital = true;
    for(auto x : s) {
        if(bCapital == true) {
            x = std::toupper(x);
        } else {
            x = std::tolower(x);
        }
        
        bCapital = !bCapital;
        answer += x;
        if(isspace(x)) bCapital = true;
    }
    return answer;
}