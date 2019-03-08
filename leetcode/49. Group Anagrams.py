# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs):
#         Runtime: 168 ms, faster than 26.88% of Python3 online submissions for Group Anagrams.
#         Memory Usage: 16.7 MB, less than 18.22% of Python3 online submissions for Group Anagrams.
        maps = {}
        for s in strs:
            cnt = [0 for i in range(26)]
            for c in s:
                cnt[ord(c)-ord('a')]+=1
            key = str(cnt)
            if key not in maps:
                maps[key]=[]
            maps[key].append(s)
        res = []
        for ans in maps:
            res.append(maps[ans])
        return res
    def groupAnagrams1(self, strs):
        # Runtime: 116 ms, faster than 77.00% of Python3 online submissions for Group Anagrams.
        # Memory Usage: 15.9 MB, less than 36.96% of Python3 online submissions for Group Anagrams.   
        dt = {}
        for st in strs:
            t = ''.join(sorted(st))
            if t in dt:
                dt[t].append(st)
            else:
                dt[t] = [st]
        return list(dt.values())
s = Solution()
i = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(i))


        