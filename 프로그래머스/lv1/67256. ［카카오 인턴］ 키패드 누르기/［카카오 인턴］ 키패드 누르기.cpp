#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int L(10), R(12);
    for(auto x : numbers) {
        if(x == 0) x = 11;
        switch(x) {
            case 1:
            case 4:
            case 7: {
                answer += "L";
                L = x;
                break;
            }
            case 3:
            case 6:
            case 9: {
                answer += "R";
                R = x;
                break;
            }
            default: {
                int a = abs(x - R);
                int b = abs(x - L);
                int disA = (a % 3) + (a / 3);
                int disB = (b % 3) + (b / 3);
                if(disB < disA) {
                    answer += "L";
                    L = x;
                } else if(disA < disB) {
                    answer += "R";
                    R = x;
                } else {
                    if (hand == "right") {
                        answer += "R";
                        R = x;
                    } else {
                        answer += "L";
                        L = x;
                    }                    
                }
                
                break;
            }
        }
    }
    return answer;
}