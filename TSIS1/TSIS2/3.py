class Solution(object):
    def numIdenticalPairs(self, nums):
        ans=0
        for i in range(len(nums)):
            k=i-1
            while k>=0:
                if nums[k]==nums[i]:
                    ans+=1
                k-=1
        return ans