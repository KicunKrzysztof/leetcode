class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for j in range(len(nums)):
            if j > max_idx:
                return False
            if max_idx <= j + nums[j]:
                max_idx  = j + nums[j]
        return True