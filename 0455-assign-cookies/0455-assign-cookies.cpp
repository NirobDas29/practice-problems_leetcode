class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int n = g.size();
        int m = s.size();
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int child = 0;
        int cookie = 0;
        int count = 0;

        while (child < g.size() && cookie < s.size()) {
            if(s[cookie]>=g[child])
            {
                child++;
                cookie++;
                count++;
            }
            else
            {
                cookie++;
            }
        }
        return count;


        
    }
};