class Solution(object):
    def asteroidCollision(self, asteroids):

        stack = []
        for asteroid in asteroids:

            if stack and asteroid < 0 and stack[-1] > 0:
                used = False
                while stack and asteroid < 0 and stack[-1] > 0:
                    if abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        used = True
                        break
                    else:
                        used = True
                        break
                if not used:
                    stack.append(asteroid)

            else:
                stack.append(asteroid)

        return stack
