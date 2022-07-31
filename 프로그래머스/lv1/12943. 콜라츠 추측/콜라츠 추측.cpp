#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    if (num == 1) return 0;
    if(num < 1 || 8000000 < num) exit(1);
    int i;
    long lnum = num;
    
    for(i = 0; i < 500; i++) {
        if( lnum % 2 == 0) {
            lnum /= 2;            
        } else {
            lnum *= 3;
            lnum += 1;            
        }
        
        if(lnum == 1) {
            break;
        }
    }
    
    if(lnum == 1 && i < 500) {
        lnum = i+1;
    } else {
        lnum = -1;
    }
    
    return lnum;
}