class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            # both sides alnum - skip both
            if not s[start].isalnum() and not s[end].isalnum():
                start+=1
                end-=1
                continue
            # only end is alnum
            elif not s[end].isalnum():
                end-=1
                continue
            # only start is alnum
            elif not s[start].isalnum():
                start+=1
                continue
            elif s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

        