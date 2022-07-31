#include <string>
#include <iostream>
using namespace std;

bool solution(string s) {
    int count = 0;

    for(auto x : s) {
        if(x == 'p' || x == 'P') {
            count++;
        } else if(x == 'y' || x == 'Y') {
            count--;            
        } else {
            // Do nothing            
        }
    }

    return count == 0 ? true : false;
}