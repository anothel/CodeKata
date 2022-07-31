#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0, sum = 0;
    
    sort(d.begin(), d.end());
    
    for(auto x : d) {
        sum += x;
        answer++;
        if(budget < sum) {
            --answer;
            break;
        }
    }

    return answer;
}