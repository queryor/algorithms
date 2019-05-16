// Given a string s, partition s such that every substring of the partition is a palindrome.

// Return the minimum cuts needed for a palindrome partitioning of s.

// Example:

// Input: "aab"
// Output: 1
// Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
using namespace std;
class Solution {
    void helper(int i, int j, const string &s, vector<int> &dp){
        for(; 0 <= i && j < s.size(); --i, ++j){
            if(s[i] != s[j]) break;
            dp[j] = min(dp[j], i > 0? dp[i - 1] + 1 : 0);
        }
    }
    
public:
    int minCut(string s) {
        vector<int> dp(s.size());
        for(int i = 0; i < dp.size(); ++i) dp[i] = i;
        for(int i = 1; i < s.size(); ++i){
            helper(i, i, s, dp);
            helper(i - 1, i, s, dp);
        }
        return dp[s.size() - 1];
    }
};