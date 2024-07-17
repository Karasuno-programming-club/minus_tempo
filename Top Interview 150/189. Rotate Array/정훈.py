class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ln = len(nums)
        k %= ln
        cnt = 0
        idx = 0
        cur = nums[idx]
        start = 0
        while cnt < ln:
            idx = (idx+k) % ln
            if idx == start:
                nums[idx], cur = cur, nums[idx]
                idx = (idx+1) % ln
                cur = nums[idx]
                start = idx
            else:
                nums[idx], cur = cur, nums[idx]
            cnt += 1
