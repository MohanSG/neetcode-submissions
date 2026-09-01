class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(str(len(word)) + "#" + word)
        return ''.join(output)
    
    #   5#Hello5#World
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            output.append(s[i:i + length])

            i += length

        return output
            