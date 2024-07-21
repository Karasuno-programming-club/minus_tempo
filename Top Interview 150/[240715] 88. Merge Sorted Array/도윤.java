class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1; //nums1 포인터
        int p2 = n - 1; //nums2 포인터
        int ep = m+n-1;

        while(p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[ep] = nums1[p1];
                ep--;
                p1--;
            } else {
                nums1[ep] = nums2[p2];
                ep--;
                p2--;
            }
        }
    }
}


