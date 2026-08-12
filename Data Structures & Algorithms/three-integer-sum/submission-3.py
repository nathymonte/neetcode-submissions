class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        output = []
        length = len(nums) - 2

        for i in range(0, length):
            fixed = nums_sort[i]
            left = i + 1
            right = len(nums) - 1
            if i != 0:
                if nums_sort[i] == nums_sort[i - 1]:
                    continue
            while left < right:
                if fixed + nums_sort[left] + nums_sort[right] == 0:
                    output.append([fixed, nums_sort[left], nums_sort[right]])
                    right -= 1
                    left += 1
                    while nums_sort[left] == nums_sort[left - 1] and left < right:
                        left += 1
                    while nums_sort[right] == nums_sort[right + 1] and left < right:
                        right -= 1               
                elif fixed + nums_sort[left] + nums_sort[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return output            
                    




