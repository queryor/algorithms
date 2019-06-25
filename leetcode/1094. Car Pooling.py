'''假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了你的第 i 次行程信息：

必须接送的乘客数量；
乘客的上车地点；
以及乘客的下车地点。
这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所用乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。
'''
import heapq
from collections import defaultdict
class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        q = []
        dic = defaultdict(int)
        trips.sort(key=lambda x:x[1])
        #print(trips)
        c = 0
        for i in range(len(trips)):
            n,s,e = trips[i]
            dic[e]+=n
            for j in range(len(q)):
                end = heapq.heappop(q)
                if end<=s:
                    c-=dic[end]
                    dic.pop(end)
                else: 
                    heapq.heappush(q,end)
                    break
            c+=n
            if c>capacity:
                return False
            heapq.heappush(q,e)
        return True


trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
trips = [[2,1,5],[3,3,7]]
capacity = 4
trips = [[7,5,6],[6,7,8],[10,1,6]]
capacity = 16
trips = [[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]]
capacity = 12
s = Solution()
print(s.carPooling(trips,capacity))