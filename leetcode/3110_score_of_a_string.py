class Solution(object):
    def scoreOfString(self, s):
        res = 0
        for i in range(0, len(s)-1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res
