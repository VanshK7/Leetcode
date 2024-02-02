import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return re.sub("[^a-zA-Z0-9]", "", s).lower() == re.sub("[^a-zA-Z0-9]", "", s[::-1]).lower()
        