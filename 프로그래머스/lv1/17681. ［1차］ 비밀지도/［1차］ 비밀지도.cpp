#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    string s;
    
    vector<vector<int>> tables1, tables2;
    vector<int> table1(n, 0), table2(n, 0);
    
    int number1 = 0;
    for(int i = 0; i < arr1.size(); i++) {
        for(int j = arr1.size() - 1; 0 <= j; j--) {
            table1.at(j) = arr1.at(i) % 2;
            arr1.at(i) /= 2;
            table2.at(j) = arr2.at(i) % 2;
            arr2.at(i) /= 2;
        }
/*
        for(auto x : table1) {
            cout << x << " ";
        }
        cout << "\n";
        
        for(auto x : table2) {
            cout << x << " ";
        }
        cout << "\n";
*/
        tables1.push_back(table1);
        tables2.push_back(table2);
    }
    
    for(int i = 0; i < tables1.size(); i++) {
        for(int j = 0; j < tables1.size(); j++) {
            if(tables1.at(i).at(j) || tables2.at(i).at(j) == 1) {
                s += "#";
            } else {
                s += " ";
            }
        }        
        answer.push_back(s);
        s.clear();
    }
    
    return answer;
}