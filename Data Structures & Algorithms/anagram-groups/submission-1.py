class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dicts = {}
        output = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in group_dicts:
                group_dicts[sorted_word] = []
                group_dicts[sorted_word].append(word)
            else:
                group_dicts[sorted_word].append(word)
        
        for group in group_dicts:
            output.append(group_dicts[group])

        return output