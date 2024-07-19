class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpable = 1
        for n in nums:
            if jumpable < 1: return False
            jumpable -= 1
            jumpable = max(jumpable, n)
        return True
