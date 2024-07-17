class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ep = len(nums) - 1
        sp = 0

        cnt = 0

        while sp <= ep :
            if nums[sp] == val:
                nums[sp], nums[ep] = nums[ep], nums[sp]
                ep -= 1
                cnt += 1
            if nums[sp] != val:
                sp += 1

        return len(nums) - cnt
