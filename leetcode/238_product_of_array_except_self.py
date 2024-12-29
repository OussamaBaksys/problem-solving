class Solution(object):
    def productExceptSelf(self, arr):
        n = len(arr)

        if n == 1:
            return [1]
        left = [1] * n
        right = [1] * n
        prod = [1] * n

        for i in range(1, n):
            left[i] = arr[i - 1] * left[i - 1]

        for j in range(n - 2, -1, -1):
            right[j] = arr[j + 1] * right[j + 1]

        for i in range(n):
            prod[i] = left[i] * right[i]

        return prod
