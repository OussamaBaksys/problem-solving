class Solution(object):
    def uniqueOccurrences(self, arr):
        occ = {}
        for el in arr:
            if el in occ:
                occ[el] += 1
            else:
                occ[el] = 1
        return len(set(arr)) == len(set(occ.values()))
