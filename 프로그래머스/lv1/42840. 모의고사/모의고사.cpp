#include <string>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

int getPerson1(const int& n) {
    array<int, 6> ggoltong{0, 1, 2, 3, 4, 5};
    int a = n % 5;
    if (a == 0) a = 5;
    return ggoltong.at(a);
}

int getPerson2(const int& n) {
    array<int, 9> ggoltong{0, 2, 1, 2, 3, 2, 4, 2, 5};
    int a = n % 8;
    if (a == 0) a = 8;
    return ggoltong.at(a);
}

int getPerson3(const int& n) {
    array<int, 11> ggoltong{0, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int a = n % 10;
    if (a == 0) a = 10;
    return ggoltong.at(a);
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> a(3, 0);
    
    for(int i = 0; i < answers.size(); i++) {
        if(answers.at(i) == getPerson1(i + 1)) {
            a.at(0)++;
        }
        if(answers.at(i) == getPerson2(i + 1)) {
            a.at(1)++;
        }
        if(answers.at(i) == getPerson3(i + 1)) {
            a.at(2)++;
        }
    }
    
    int max = 0;
    if(max <= a.at(0)) {
        max = a.at(0);
    }
    if(max <= a.at(1)) {
        max = a.at(1);
    }
    if(max <= a.at(2)) {
        max = a.at(2);
    }    
    
    if(max == 0) max = -1;

    for(int i = 0; i < a.size(); i++) {
        if(max == a.at(i)) {
            answer.push_back(i+1);            
        }        
    }

    return answer;
}