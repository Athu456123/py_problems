    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)
        for i in range(end-1):
            for j in range(i+1,end):
                if nums[i] + nums[j] == target:
                    return(i,j)