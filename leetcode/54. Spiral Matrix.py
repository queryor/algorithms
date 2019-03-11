# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix):
        ans = []
        def spiralOrderDFS(matrix):
            #print(matrix)
            if len(matrix)==0 or len(matrix[0])==0:
                return 0
            elif len(matrix)==1:
                for num in matrix[0]:
                    ans.append(num)
            elif len(matrix[0])==1:
                for i in range(len(matrix)):
                    ans.append(matrix[i][0]) 
            else: 
                for num in matrix[0]:
                    ans.append(num)
                #print(ans)
                for i in range(1,len(matrix)):
                    ans.append(matrix[i][-1])
                for i in range(len(matrix[0])-2,-1,-1):
                    ans.append(matrix[-1][i])
                for i in range(len(matrix)-2,0,-1):
                    ans.append(matrix[i][0])
                t = matrix[1:-1]
                for nums in t:
                    nums.pop()
                    nums.pop(0)
                spiralOrderDFS(t)
        spiralOrderDFS(matrix)
        return ans




s = Solution()
i = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

print(s.spiralOrder(i))        