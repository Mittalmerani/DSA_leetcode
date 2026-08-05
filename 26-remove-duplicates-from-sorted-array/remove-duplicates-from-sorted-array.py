class Solution(object):
    def removeDuplicates(self, nums):
        result = sorted(set(nums))

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)


object = Solution()
print(object.removeDuplicates)