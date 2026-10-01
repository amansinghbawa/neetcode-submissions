class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        f = 0
        l = len(nums) - 1
        while (f < l-1):
            m = (l + f) // 2
            print(f, l, m)
            if nums[f] < nums[l]:
                return nums[f]
            else:
                if nums[m] > nums[l]:
                    f = m
                else:
                    l = m
        return nums[f] if nums[f] < nums[l] else nums[l]




        