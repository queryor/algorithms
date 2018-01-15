
// 题目描述
// 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
// 例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
// 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

//题解 就是一层层输出  注意处理好只有一列和一行的情况

class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int>res;
        res.clear();
        int row=matrix.size();//行数
        int collor=matrix[0].size();//列数
        for(int count=0;;count++){
            int rowM = row - count*2;
            int colM = collor - count*2;
            if(rowM<=0 || colM<=0)break;
            int i=count,j=count;
            for(int m=0;m<colM;m++)
                res.push_back(matrix[i][m+j]);
            for(int m=1;m<rowM;m++)
                res.push_back(matrix[m+i][colM-1+j]);
            if(rowM>1&&colM>1){
            	for(int m=colM-2;m>=1;m--)
                    res.push_back(matrix[rowM-1+i][m+j]);
                for(int m=rowM-1;m>=1;m--)
                    res.push_back(matrix[m+i][j]);
            }
        }
        return res;
    }
};