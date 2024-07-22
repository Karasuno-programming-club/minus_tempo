class Solution {
    public int hIndex(int[] citations) {
        int h = citations.length;
        int maxi = 0;
        Arrays.sort(citations);
        for (int i = 0; i < h; i++) {
            // 밑에서부터 위쪽으로 남은 논문 수보다
            // 현재 인덱스의 인용수가 크면
            if (citations[i] >= h-i)
                // 남은 논문 개수가 새로운 최대값
                maxi = Math.max(maxi,h-i);
        }
        return maxi;
    }
}
