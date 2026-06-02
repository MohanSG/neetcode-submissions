class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #Create a frequency dict
        output = [] #Output array

        for i in range(len(nums)): #Loop through nums
            if nums[i] not in freq: #Count the frequency of each number, store as  freq[number] = count
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        buckets = [[] for _ in range(len(nums) + 1)] #Creates buckets == length of nums array + 1

        for num, count in freq.items(): 
            buckets[count].append(num) #using the count as index, append the number to the buckets

        for num in reversed(buckets): #Loop through reversed array to sort frequency
            if num: #If a number exists in the array
                for i in range(len(num)): #Some buckets may have multiple elements
                    output.append(num[i]) #append to output
                if len(output) == k: #Check that the length of output doesnt exceed k
                    return output