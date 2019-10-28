class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> bitCount;
        bitCount.push_back(0);
        for(int i=1;i<=num;i++) {
            bitCount.push_back((i&1) + bitCount[i>>1]);
            }
        return bitCount;
    }
};