'''There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''

class Solution:
    def candy(self, ratings) -> int:
        ## 超时 O(n^2)
        n =len(ratings)
        candy_list = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candy_list[i] = candy_list[i-1]+1
            elif ratings[i]==ratings[i-1]:
                candy_list[i] = 1
            else: 
                candy_list[i] = 1
                if candy_list[i-1]==1:
                    for j in range(i-1,-1,-1):
                        if ratings[j]>ratings[j+1] and candy_list[j]<=candy_list[j+1]:
                            candy_list[j]+=1
                        else: 
                            break
        return sum(candy_list)
    def candy1(self, ratings) -> int:
        ## 两层for 循环
        ## 第一个循环保证右边比左边投票大的 糖果多
        ## 第一个循环保证左边比右边投票大的 糖果多
        n = len(ratings)
        candy_list = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                candy_list[i] = candy_list[i-1]+1
        for i in range(n-1,0,-1):
            if ratings[i-1] >ratings[i]:
                candy_list[i-1] = max(candy_list[i-1],candy_list[i]+1)
        return sum(candy_list)
    def candy2(self,ratings):
        # 下面来看一次遍历的方法，相比于遍历两次的思路简单明了，这种只遍历一次的解法就稍有些复杂了。首先我们给第一个同学一个糖果，那么对于接下来的一个同学就有三种情况：

        # 1. 接下来的同学的rating等于前一个同学，那么给接下来的同学一个糖果就行。

        # 2. 接下来的同学的rating大于前一个同学，那么给接下来的同学的糖果数要比前一个同学糖果数加1。

        # 3.接下来的同学的rating小于前一个同学，那么我们此时不知道应该给这个同学多少个糖果，需要看后面的情况。

        # 对于第三种情况，我们不确定要给几个，因为要是只给1个的话，那么有可能接下来还有rating更小的同学，总不能一个都不给吧。也不能直接给前一个同学的糖果数减1，有可能给多了，因为如果后面再没人了的话，
        # 其实只要给一个就行了。还有就是，如果后面好几个rating越来越小的同学，那么前一个同学的糖果数可能还得追加，以保证最后面的同学至少能有1个糖果。来一个例子吧，四个同学，他们的rating如下：

        # 1 3 2 1

        # 先给第一个rating为1的同学一个糖果，然后从第二个同学开始遍历，第二个同学rating为3，比1大，所以多给一个糖果，第二个同学得到两个糖果。下面第三个同学，他的rating为2，比前一个同学的rating小，
        # 如果我们此时给1个糖果的话，那么rating更小的第四个同学就得不到糖果了，
        # 所以我们要给第四个同学1个糖果，而给第三个同学2个糖果，此时要给第二个同学追加1个糖果，使其能够比第三个同学的糖果数多至少一个。
        # 那么我们就需要统计出多有个连着的同学的rating变小，用变量cnt来记录，找出了最后一个减小的同学，那么就可以往前推，每往前一个加一个糖果，这就是个等差数列，
        # 我们可以直接利用求和公式算出这些rating减小的同学的糖果之和。
        # 然后我们还要看第一个开始减小的同学的前一个同学需不需要追加糖果，只要比较cnt和pre的大小，pre是之前同学得到的最大糖果数，二者做差加1就是需要追加的糖果数，加到结果res中即可
        pass

            
s = Solution()
input = [1,2,3,1,0]
# input = [1,3,2,2,1]
# # input = [1,6,10,8,7,3,2]

print(s.candy1(input))