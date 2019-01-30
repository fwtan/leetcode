class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        best_lengths = [1] * n
        best_lengths[-1] = 1
        max_len = 1
        for i in range(n-1, -1, -1):
            curr_val = nums[i]
            for j in range(i+1, n):
                next_val = nums[j]
                if curr_val < next_val and best_lengths[i] < best_lengths[j] + 1:
                    best_lengths[i] = best_lengths[j] + 1
                    if max_len < best_lengths[i]:
                        max_len = best_lengths[i]
        return max_len