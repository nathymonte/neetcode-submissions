class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        cont = []
        nums = set(nums)

        if not nums:
            return 0
        
        for num in nums:
            m = num - 1
            if m not in nums:
                plus = 1
                dic[num] = [num]
                while True:
                    n = num + plus                    
                    if n in nums:
                        dic[num].append(n)
                        plus += 1
                    else:
                        break            

        for key in dic:
            cont.append(len(dic[key]))

        result = max(cont)
        return result        
