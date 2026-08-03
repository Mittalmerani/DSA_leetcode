class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        exp = n*(n+1) /2

        total = sum(nums)
        result = exp - total
        return result
object = Solution()
print(object.missingNumber)
        