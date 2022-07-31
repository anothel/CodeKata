#include <string>
#include <vector>
#include <clocale>
#include <iostream>

using namespace std;

string solution(string new_id) {
    // step 1
    for(int i = 0; i < new_id.length(); i++) {
        char &c = new_id.at(i);
        if(isupper(c)) {
            c = tolower(c);
            // cout << "step1: new_id: " << new_id << endl;
        }
    }
    
    // step 2    
    for(int i = 0; i < new_id.length(); i++) {
        char &c = new_id.at(i);
        if(!islower(c) && !isdigit(c) && c != '-' && c != '_' && c != '.') {
            new_id.erase(new_id.begin() + i--);
            // cout << "step2: new_id: " << new_id << endl;
        }
    }
    
    // step 3
    for(int i = 0; i < new_id.length(); i++) {
        char &c = new_id.at(i);
        if(c == '.' && i + 1 <= new_id.length() - 1) {
            if(new_id.at(i + 1) == '.') {
                new_id.erase(new_id.begin() + i--);
                // cout << "step3: new_id: " << new_id << endl;
            }
        }
    }
    
    // step 4    
    for(int i = 0; i < new_id.length(); i++) {
        if(new_id.at(new_id.length() - 1) == '.' || new_id.at(0) == '.') {
            if(new_id.at(new_id.length() - 1) == '.') {
                new_id.erase(new_id.begin() + new_id.length() - 1); 
            } else {
                new_id.erase(new_id.begin() + 0);
            }
            i--;
            // cout << "step4: new_id: " << new_id << endl;
        }
    }
    
    // step 5
    if(new_id.length() == 0) {
        new_id += "a";        
    }
    
    // step 6
    if(16 <= new_id.length()) {
        new_id.erase(new_id.begin() + 15, new_id.end());
    }
    if(new_id.at(new_id.length() - 1) == '.') {
        new_id.erase(new_id.begin() + new_id.length() - 1);
    }
    
    // step 7
    if(new_id.length() <= 2) {
        while(new_id.length() < 3) {
            new_id += new_id.at(new_id.length() - 1);
        }
    }    

    // cout << "final new_id: " << new_id << endl;
    
    return new_id;
}