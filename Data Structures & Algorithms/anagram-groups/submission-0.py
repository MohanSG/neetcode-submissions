class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        output = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
                groups[sorted_word].append(word)
            else:
                groups[sorted_word].append(word)
        
        for key in groups:
            output.append(groups[key])
        
        return output