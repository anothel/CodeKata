#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    map<string, vector<string>> select;
    map<string, int> selected;
    
    for(auto x : report) {
        std::istringstream ss(x);
        std::string token;
        
        bool bSecond = false;
        string tmpToken;

        while(std::getline(ss, token, ' ')) {
            if(bSecond == true) {
                bool bSame = false;
                for(auto y : select[tmpToken]) {
                    // cout << "tmpToken: " << tmpToken << ", token: " << token << ", y: " << y << endl;
                    if(y == token) bSame = true;                    
                }
                if(bSame) break;
                selected[token]++;
                // cout << "selected[" << token << "]: " << selected[token] << endl;
            } else {
                bSecond = true;
                tmpToken = token;
                continue;
            }
            // cout << "x: " << x << ", " << "token: " << token << endl;
            select[tmpToken].push_back(token);
            // cout << "select[" << tmpToken << "].size(): " << select[tmpToken].size() << endl;
        }        
    }
    
    for(auto x : id_list) {
        // cout << "x: " << x << endl;
        int count = 0;
        // cout << "select[x].size(): " << select[x].size() << endl;
        for(auto y : select[x]) {
            // cout << "y: " << y << endl;
            if(k <= selected[y]) {
                count++;                
            }            
        }
        answer.push_back(count);
    }
    return answer;
}