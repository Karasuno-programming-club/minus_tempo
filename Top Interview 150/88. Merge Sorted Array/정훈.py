class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1 = nums1[:]
        n2 = nums2[:]

        p1 = 0
        p2 = 0
        pn = 0
        for _ in range(m+n):
            if p1 < m:
                if p2 >= n or n1[p1] < n2[p2]:
                    sml = n1[p1]
                    p1 += 1
                else:
                    sml = n2[p2]
                    p2 += 1
            else:
                sml = n2[p2]
                p2 += 1
            nums1[pn]=sml
            pn += 1
