class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int ans[] = new int[n];
        Arrays.fill(ans, 1);
        // 앞 뒤로 누적곱 구하기

        // e.g. 1 2 3
        int cur = 1;
        for (int i = 0; i < n; i++) {
            ans[i] *= cur;
            cur *= nums[i];
        }
        // 1 1 1
        // 1 1 1
        // 1 1 1
        // 1 1 2
        cur = 1;
        for (int i = n-1; i>=0; i--) {
            ans[i] *= cur;
            cur *= nums[i];
        }
        // 1 1 2
        // 1 1 2
        // 1 3 2
        // 6 3 2
        return ans;
    }
}
