#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
	vector<int> singleNumber(vector<int>& nums) {
		unordered_set<int> s;
		for (auto n:nums) {
			if (s.count(n) == 0)
				s.insert(n);
			else
				s.erase(n);
		}
		vector<int> a;
		for (auto n : nums) {
			a.push_back(n);
		}
		return a;
	}
};
int main() {
	vector<int> i = {1, 2, 3, 4, 0};
	Solution s;
	vector<int> ans = s.singleNumber(i);
	cout<<ans[0]<<ans[1]<< endl;
	system("pause");
	return 0;
}