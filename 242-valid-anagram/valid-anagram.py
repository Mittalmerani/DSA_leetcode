class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
object = Solution()
print(object.isAnagram)