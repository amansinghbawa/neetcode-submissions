from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        product_of_all = reduce(lambda x,y: x*y, nums, 1)
        if product_of_all:
            nums = [product_of_all//num for num in nums]
        else:
            product_of_all = reduce(lambda x,y: x*y, filter(lambda n: n!= 0, nums), 1)
            nums = [product_of_all if num == 0 else 0 for num in nums ]
        return nums
