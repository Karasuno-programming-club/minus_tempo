public class 도윤 {
    public int removeElement(int[] nums, int val) {

        int ep = nums.length - 1;
        int sp = 0;
        int cnt = 0;

        while(sp <= ep) {
            if(nums[sp] == val) {
                nums[sp] = nums[ep--] ;
                cnt++;
            } else {
                sp++;
            }

        }

        return nums.length - cnt;
    }
}
