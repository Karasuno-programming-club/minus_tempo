class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ns = set()

        cnt = 0
        for n in nums:
            if n not in ns:
                nums[cnt] = n
                ns.add(n)
                cnt += 1

        return cnt
