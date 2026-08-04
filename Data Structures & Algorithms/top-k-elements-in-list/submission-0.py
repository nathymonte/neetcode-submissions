class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        fr_dic = {}
        final_list = []
        for i in range(len(nums)):          
            fr_dic[nums[i]] = fr_dic.get(nums[i], 0) + 1
        
        sort_dic = dict(sorted(fr_dic.items(), key=lambda item: item[1], reverse=True))

        for j in range(k):
            final_list.append(list(sort_dic)[j])

        return final_list


        