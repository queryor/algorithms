"""Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s: str):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ##DFS
        ans = []
        self.dfs(0, [], s, ans)
        return ans

    def dfs(self, cur, cur_list, s, ans):
        if cur == len(s):
            ans.append(cur_list)
            return

        for i in range(cur, len(s)):
            t = s[cur:i + 1]
            if t == t[::-1]:
                self.dfs(i + 1, cur_list + [t], s, ans)