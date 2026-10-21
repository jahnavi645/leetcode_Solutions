class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Extra full rotations do not change the array

        # Reverse the whole list
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the rest
        nums[k:] = reversed(nums[k:])
       