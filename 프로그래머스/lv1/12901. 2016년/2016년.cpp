#include <string>
#include <vector>

#include <map>

using namespace std;

map<int, string> days = {{3,"SUN"}, {4, "MON"}, {5, "TUE"}, {6, "WED"}, {0, "THU"}, {1, "FRI"}, {2, "SAT"}};

map<int, int> month = {{0, 0}, {1, 31}, {2, 29}, {3, 31}, {4, 30}, {5, 31}, {6, 30}, {7, 31}, {8, 31}, {9, 30}, {10, 31}, {11, 30}, {12, 31}};

string solution(int a, int b) {
    int day = 0;    
    for(int i = 0; i < a; i++) {
        day += month[i];
    }
    
    return days[(day + b) % 7];
}