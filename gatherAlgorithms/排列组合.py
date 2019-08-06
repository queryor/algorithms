
### python 排列组合接口
import itertools
if __name__ == "__main__":
    ## 组合
    print(list(itertools.combinations("abcd",2)))
    ## 排列
    print(list(itertools.permutations("abcd",2)))