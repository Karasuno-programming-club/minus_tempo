class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = 1
        zcnt = 0
        for n in nums:
            if n==0:
                zcnt += 1
                continue
            prd *= n
        if zcnt > 1:
            return [0 for _ in range(len(nums))]
        if zcnt > 0:
            return [ 0 if n != 0 else prd for n in nums]
        answer=[]
        for n in nums:
            answer.append(int(prd/n))
        return answer
        
