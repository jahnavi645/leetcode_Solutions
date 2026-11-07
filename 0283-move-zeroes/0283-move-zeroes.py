class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)

        slow = 0

        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow,n):
            nums[i] = 0

        return nums    




        

