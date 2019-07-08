class Solution:
    def twoSum(self, nums, target):
        for index, item in enumerate(nums):
            if (target-item) in nums:
                if index == nums.index(target-item):
                    continue
                else:
                    return [index, nums.index(target-item)]

