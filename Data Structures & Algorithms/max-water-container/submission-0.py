class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        areas = []
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            a = w * h
            areas.append(a)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max(areas)        

"""
tracing mental:
0 - 7: w = 7, h = 1, a = 7
1 - 7: w = 6, h = 6, a = 36
1 - 6: w = 5, h = 3, a = 15
1 - 5: w = 4, h = 7, a = 28
1 - 4: w = 3, h = 1, a = 3
1 - 3: w = 2, h = 5, a = 10
1 - 2: w = 1, h = 2, a = 2
"""