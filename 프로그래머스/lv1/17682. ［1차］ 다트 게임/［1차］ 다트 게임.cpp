#include <string>
#include <vector>
#include <cmath>

using namespace std;

bool isOption(char c) {
    return c == '*' || c == '#' ? true : false;
}

int solution(string dartResult) {
    int answer = 0;
    vector<int> st, st_answer;
    int minus = 0;
    char c, special;
    
    while(0 < dartResult.length()) {
        c = dartResult.at(0);
        
        if(1 < dartResult.length()) {
            special = dartResult.at(1);
        }
        
        if( '0' <= c && c <= '9' ) {
            if(c == '1' && dartResult.at(1) == '0') {
                dartResult = dartResult.substr(1);
                st.push_back(10);
            } else {
                st.push_back(c - 48);
            }
        } else if( 'S' == c || 'D' == c || 'T' == c) {
            minus = 1;
            if( special == '#' ) {
                minus = -1;                
            }
            
            switch(c) {
                    case 'S': {
                        st_answer.push_back(minus * pow(st.back(), 1));
                        break;
                    }
                    case 'D': {
                        st_answer.push_back(minus * pow(st.back(), 2));
                        break;
                    }
                    case 'T': {
                        st_answer.push_back(minus * pow(st.back(), 3));
                        break;
                    }
                    default: {
                        // Do nothing
                        break;
                    }   
            }
            
            if(special == '*') {
                int count = 0;
                for(int i = st_answer.size() - 1; 0 <= i; i-- ) {
                    st_answer[i] *= 2;
                    if (++count == 2) break;
                }
            }
            
        } else {
            
        }
        dartResult = dartResult.substr(1);
    }
    
    for(auto x : st_answer) answer += x;
        
    return answer;
}