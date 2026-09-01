class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {} #Make a new dictionary
        output = []
        
        for i in range(len(nums)): #Loop through input array
            num = nums[i]
            if num in nums_dict:
                nums_dict[num] += 1 #For every number in input array, add value to dict with 
                                    #num as key and value as freq. increment by 1 if exists
            else:
                nums_dict[num] = 0 #If num doesn't exist in dict yet, add it increment by 1
                nums_dict[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)] #Create buckets, length of input array
                                                     #+ 1
        
        for nums in nums_dict: #loop through dict keys 
            freq = nums_dict[nums] #get the frequency
            buckets[freq].append(nums) #append nums to frequency as index
        
        for freq in range(len(buckets) -1, 0, -1): #Loop through buckets, reversing index
            for num in buckets[freq]: #Nested loop so loop again
                output.append(num) #append number to output
                if len(output) == k: #If the length of output is equal to k we have all k most frequent numbers
                    return output 