#coding:gb2312
'''
leetcode: Group Anagrams
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        strs.sort()

        same_str = {}
        same_index = 0

        result = []

        for i in range(len(strs)):
            str_list = list(strs[i]) # 将字符串先转换成列表
            str_list.sort()

            temp_str = "".join(str_list)
            if temp_str in same_str:
                result[same_str[temp_str]].append(strs[i])
            else:
                same_str[temp_str] = same_index
                temp = []
                temp.append(strs[i])
                result.append(temp)
                same_index += 1

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
