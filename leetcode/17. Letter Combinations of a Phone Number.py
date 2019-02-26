# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str):
        res = []
        dict = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        self.letterCombinationsDFS(digits,dict,0,"",res)
        return res
    def letterCombinationsDFS(self,digits,dict,level,out,res):
        if(level==len(digits)):
            if out != "":   
                res.append(out)
            return 0
        str = dict[int(digits[level])-int('0')]
        for c in str:
            self.letterCombinationsDFS(digits,dict,level+1,out+c,res)

    def letterCombinations1(self, digits):
        letter_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:return []
        out_list = list(letter_dict[digits[0]])
        for num in digits[1:]:
            out_list = self.func(letter_dict[num],out_list)
        return out_list
    def func(self, letter_str, out_list):
        letter_list = list(letter_str)
        return [a+b for a in out_list for b in letter_list]


s  = Solution()
a ="12"
print(s.letterCombinations(a))