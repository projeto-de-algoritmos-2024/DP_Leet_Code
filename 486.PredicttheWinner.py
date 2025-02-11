class Solution(object):

    def predictTheWinner(self, nums):
        memo = {}
        return self.run(0, len(nums) - 1, nums, memo) >= 0

    def run(self, left, right, nums, memo):
        if left == right:
            return nums[left]

        if (left, right) in memo:
            return memo[(left, right)]

        pick_left = nums[left] - self.run(left + 1, right, nums, memo)
        pick_right = nums[right] - self.run(left, right - 1, nums, memo)

        memo[(left, right)] = max(pick_left, pick_right)
        return memo[(left, right)]
