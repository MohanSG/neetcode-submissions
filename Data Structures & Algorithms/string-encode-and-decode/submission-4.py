class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)) + "#" + word)
        print(parts)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded_string = ""
        str_length = ""
        output = []

        i = 0
        while i < (len(s)):
            while s[i] != "#":
                str_length += s[i]
                i += 1
            
            length = int(str_length)
            for j in range(i+1, i+1+length):
                decoded_string += s[j]
            
            i += 1 + length

            output.append(decoded_string)

            decoded_string = ""
            str_length = ""
        return output