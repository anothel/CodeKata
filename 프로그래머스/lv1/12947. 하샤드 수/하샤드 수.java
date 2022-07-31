class Solution {
    public boolean solution(int x) {
        int _x = x;
        int sum = 0;
        
        while(0 < x) {
            sum += x % 10;
            x /= 10;
        }
        
        return (_x % sum) == 0 ? true : false;
    }
}