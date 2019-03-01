#include<iostream>
us namespace std;
class Solution {
public:
	vector<int> findSubstring(string s, vector<string>& words) {
		vector<int> ans;
		if (s.empty() || words.empty()) return ans;

		int word_len = words[0].size();
		int n = words.size();
		unordered_map<string, int> count_word;
		for (const string &word : words)
			++count_word[word];

		for (int i = 0; i + n * word_len <= s.size(); ++i) {
			int total_in = 0;
			unordered_map<string, int> cur_cnt;

			for (int j = i; j < i + n * word_len; j += word_len) {
				string word = s.substr(j, word_len);
				if (++cur_cnt[word] > count_word[word]) break;
				++total_in;
			}
			if (total_in == n)
				ans.push_back(i);
		}
		return ans;
	}
};
