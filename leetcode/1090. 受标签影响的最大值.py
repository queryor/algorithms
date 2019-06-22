'''我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。

我们从这些项中选出一个子集 S，这样一来：

|S| <= num_wanted
对于任意的标签 L，子集 S 中标签为 L 的项的数目总满足 <= use_limit。
返回子集 S 的最大可能的 和。

示例 1：

输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。
示例 2：

输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。
示例 3：

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
输出：16
解释：选出的子集是第一项和第四项。
示例 4：

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
输出：24
解释：选出的子集是第一项，第二项和第四项。
'''
import collections
import heapq
class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        hq = []
        limit = collections.defaultdict(int)
        for value, label in zip(values, labels):
            heapq.heappush(hq, (-value, label))
            limit[label] = use_limit
        ans = 0
        count = 0
        while count < num_wanted and len(hq) > 0:
            while len(hq) > 0 and limit[hq[0][1]] == 0:
                heapq.heappop(hq)
            if len(hq) > 0:
                val, lbl = heapq.heappop(hq)
                val = -val
                ans += val
                count += 1
                limit[lbl] -= 1
        return ans