class Solution(object):
    def largestAltitude(self, gain):
        max_altitude = 0
        current_altitude = 0
        for height in gain:
            current_altitude += height
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude
