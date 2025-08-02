class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=""
        for char in s:
            if char.isalpha() or char.isdigit():
                res=res+char.lower()
        print(res)
        return res==res[::-1]
