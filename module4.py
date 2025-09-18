import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone_map = {
            '2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz' 
        }
        res = []
        ls_of_letters = [phone_map[d] for d in digits]
        for combo in itertools.product(*ls_of_letters):
            ans = "".join(combo)
            res.append(ans)
        return res
    
sol = Solution()
print(sol.letterCombinations("32"))