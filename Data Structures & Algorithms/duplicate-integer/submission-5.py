class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {} #Create a dictionary
        for i in range(len(nums)): #Loop through nums
            if nums[i] in dict: #If nums[i] exists in dictionary
                dict[nums[i]] += 1 #Add 1 the number count ()
                return True
            else:
                dict[nums[i]] = 1 #If it doesn't exists, add to dict and give it a value of 1 (e.g. {1: 1})

        # for value in dict.values(): #Go over each value in the dictionary
        #     if value > 1: #if any elements value is more than 1, its a duplicate. Return True
        #         return True

        return False #If no duplicates were found, return False