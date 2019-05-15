#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
using namespace std;
class Solution {
    bool is_palindrome(const string &s, int i, int j){
        for(;i < j; ++i, --j){
            if(s[i] != s[j]) return false;
        }
        return true;
    }
    
    void dfs(int start, const string &s,  vector<vector<string>> &ans, vector<string> &cur){
        if(start == s.size()){
            ans.push_back(cur);
            return;
        }
        for(int i = start; i < s.size(); ++i){
            if(start == i || is_palindrome(s, start, i)){
                cur.push_back(s.substr(start, i - start + 1));
                dfs(i + 1, s, ans, cur);
                cur.pop_back();
            }
        }
    }
    
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> cur;
        dfs(0, s, ans, cur);
        return ans;
    }
};