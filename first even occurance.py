class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums:
            if(i%2==0):
                if(nums.count(i)==1):
                    return i
                    break
        else:
            return -1 

OUTPUT:
Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.
