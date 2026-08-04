class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_sort = {}
        final_list = []

        for i in range(len(strs)):            
            sort = "".join(sorted(strs[i]))
            if sort in dic_sort:
                dic_sort[sort].append(strs[i])
            else:
                dic_sort[sort] = [strs[i]]

        for k in dic_sort:
            temp_list = dic_sort[k]
            final_list.append(temp_list)
        return final_list