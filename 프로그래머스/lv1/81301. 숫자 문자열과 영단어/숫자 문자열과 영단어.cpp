#include <string>
#include <vector>
#include <cmath>
#include <array>
#include <algorithm>
#include <iostream>

using namespace std;

std::size_t searchWord(string s, string x) {
    return s.find(x);
}

int solution(string s) {
    array<string, 10> words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    for(int i = 0; i < words.size(); i++) {
        std::size_t pos = searchWord(s, words.at(i));
        if (std::string::npos != pos) {
            s.erase(pos, words.at(i).length());
            s.insert(pos, to_string(i--));
        }
    }
    
    return stoi(s);
}