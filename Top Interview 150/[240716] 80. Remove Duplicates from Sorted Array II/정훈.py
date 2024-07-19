class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curNum=nums[0]
        curCnt=1
        curIdx=1
        for i in range(1,len(nums)):
            if nums[i] == curNum:
                curCnt += 1
                if curCnt <= 2:
                    nums[curIdx] = curNum
                    curIdx += 1
            else:
                curNum = nums[i]
                curCnt = 1
                nums[curIdx] = curNum
                curIdx += 1
        return curIdx
            
