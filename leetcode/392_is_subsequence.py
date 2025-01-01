class Solution(object):
    def isSubsequence(self, s, t):
        start, index = 0, 0
        for char in s:
            index = - 1
            for j in range(start, len(t)):
                if t[j] == char:
                    index = j
                    break
            if index == -1:
                return False
            start = index + 1
        return True
