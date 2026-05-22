class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_string = list(''.join(e for e in s if e.isalnum()))
        left = 0
        right = len(list_string) - 1

        print(list_string)

        while left < right:
            print(left, right)
            if list_string[left].lower() == list_string[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True