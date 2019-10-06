class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            if target - n in num_dict:
                return [i, num_dict[target - n]]
            num_dict[n] = i