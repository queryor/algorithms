#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
	int findMin(vector<int>& num) {
		int left = 0, right = num.size() - 1;
		if (num[left] > num[right]) {
			while (left != (right - 1)) {
				int mid = (left + right) / 2;
				if (num[left] < num[mid]) left = mid;
				else right = mid;
			}
			return min(num[left], num[right]);
		}
		return num[0];
	}
};
int main() {
	vector<int> i = {1, 2, 3, 4, 0};
	Solution s;
	cout << s.findMin(i) << endl;
	system("pause");
	return 0;
}