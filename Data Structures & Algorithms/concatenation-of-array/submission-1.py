class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [num for _ in range(2) for num in nums]       

        return ans