class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int sum = n*(n+1)/2;
        int h_sum =0;
        for (int i: nums)
        {
            h_sum = h_sum +i;
        }
        return sum - h_sum ;

        
    }
};