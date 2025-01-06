from collections import deque


class Solution(object):
    def removeStars(self, s):

        queue = deque([])
        for char in s:
            if char == "*" and queue:
                queue.pop()
            else:
                queue.append(char)
        return "".join(queue)
