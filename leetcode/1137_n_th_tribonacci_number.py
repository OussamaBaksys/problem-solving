class Solution(object):
    def tribonacci(self, n):
        cache = [0, 1, 1]
        for i in range(3, n + 1):
            cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])
        return cache[n]