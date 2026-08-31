class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in nums_dict and nums_dict[diff] != i:
                return [i, nums_dict[diff]]
        
        return [0, 0]

      #Add list into dictionary { num : index}
        #Loop through nums
        #Get target - nums[i] as diff
        #If diff is in nums_dict and if diff is not the number we are looping through