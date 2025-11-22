from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            max_len = min(len(common), len(strs[i]))
            common = common[0 : max_len]
            for j in range(max_len):
                if common[j] == strs[i][j]:
                    continue
                else:
                    common = common[0 : j]
                    break
        return common
    

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))