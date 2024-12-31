class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        l = len(words) - 1
        res = [words[l - i] for i in range(l + 1)]
        return " ".join(res)
