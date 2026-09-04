class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        string_set = set()

        for right in range(len(s)): #z
            while s[right] in string_set: #z is not in string set, so carry on
                string_set.remove(s[left])
                left += 1
            string_set.add(s[right]) #add z to the string set
            longest = max(longest, right - left + 1)

        return longest