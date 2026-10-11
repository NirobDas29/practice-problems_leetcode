class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int maxsum = 0;
        int minsum =0;
        int currentmin =0;
        int currentmax =0;
        for (int num:nums)
        {
            currentmax = max(currentmax+num,num);
            maxsum = max(maxsum,currentmax);
            currentmin = min(currentmin+num,num);
            minsum= min(minsum,currentmin);
        }
        return max(maxsum,abs(minsum));
        
    }
};