class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                s_new += letter.lower()
        
        start = 0
        s_len = len(s_new)
        end = s_len - 1
        print(s_new)
        if s_len == 1:
            return True

        while start < end:
            if s_new[start] != s_new[end]:
                return False
            start += 1
            end -= 1
        return True

        