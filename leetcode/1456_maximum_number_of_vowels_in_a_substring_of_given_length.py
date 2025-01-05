class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        for char in s[:k]:
            if char in vowels:
                vowel_count += 1
        count = vowel_count
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1
            if count > vowel_count:
                vowel_count = count
        return vowel_count
