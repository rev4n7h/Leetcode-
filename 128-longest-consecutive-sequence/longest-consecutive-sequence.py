class Solution(object):
    def longestConsecutive(self, nums):
        set_nums = set(nums)
        longest = 0
        for i in set_nums :
            if i-1 not in set_nums:
                lenght = 0
                while i + lenght in set_nums :
                    lenght += 1
                    longest = max(longest,lenght)
                    

        return longest