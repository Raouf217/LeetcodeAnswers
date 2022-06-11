class Solution(object):
    def lengthOfLongestSubstring(self, string):
        """
        :type s: str
        :rtype: int
        """
        # i =0
        # j = 0
        # d={}
        # ans = 0
        # while j < len(s):
        #     if s[j] not in d or i>d[s[j]]:
        #         ans = max(ans,(j-i+1))
        #         d[s[j]] = j
        #     else:
        #         i = d[s[j]]+1
        #         ans = max(ans,(j-i+1))
        #         j-=1
        #     #print(ans)
        #     j+=1
        # return ans
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(0, len(string)):
            if string[i] in last_idx:
                start_idx = max(start_idx, last_idx[string[i]] + 1)
            max_len = max(max_len, i-start_idx + 1)
            last_idx[string[i]] = i
        return max_len