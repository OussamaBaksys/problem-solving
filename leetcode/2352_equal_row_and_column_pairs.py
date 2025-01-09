class Solution(object):
    def equalPairs(self, grid):
        mapping = {}
        for row in range(grid):
            key = tuple(row)
            if key in mapping:
                mapping[key] += 1
            else:
                mapping[key] = 1
        counter = 0
        for col in zip(*grid):
            if col in mapping:
                counter += mapping[col]
        return counter
