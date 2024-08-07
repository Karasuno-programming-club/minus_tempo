class Solution {
    public int jump(int[] nums) {
        int near = 0, far = 0, jumps = 0;

        while (far < nums.length - 1) {
            int farthest = 0;
            // 현재 위치부터 접근 가능한 위치까지 갈 수 있는 가장 먼 곳을 구한다
            for (int i = near; i <= far; i++)
                farthest = Math.max(farthest, i + nums[i]);
            // 왼쪽 포인터를 한칸 옮긴다
            near = far + 1;
            // 접근 가능한 위치를 갈 수 있는 가장 먼 곳으로 재설정
            far = farthest;
            // 점프
            jumps++;
            // 점프 후 가장 먼 곳이 마지막 인덱스를 넘어서면 도달한 것으로 판단하고 루프 탈출
        }

        return jumps;
    }
}
