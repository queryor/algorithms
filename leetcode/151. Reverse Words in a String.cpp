#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
#include <stack>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int storeIndex = 0, n = s.size();
        reverse(s.begin(), s.end());
        for (int i = 0; i < n; ++i) {
            if (s[i] != ' ') {
                if (storeIndex != 0) s[storeIndex++] = ' ';
                int j = i;
                while (j < n && s[j] != ' ') s[storeIndex++] = s[j++];
                reverse(s.begin() + storeIndex - (j - i), s.begin() + storeIndex);
                i = j;
            }
        }
        s.resize(storeIndex);
        return s;
    }
};