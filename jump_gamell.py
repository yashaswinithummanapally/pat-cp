class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        for i in range(len(nums) -2,-1,-1):
            if(nums[i] == 0):
                res[i] = 0
                continue
            if i+nums[i] >= len(nums) -1:
                res[i] = 1
            else:
                min = sys.maxsize
                for x in range(nums[i]):
                    if res[x+i+1] != 0 and res[x+i+1] < min:
                        min = res [x+i+1]
                res[i] = min+1
        return res[0]
