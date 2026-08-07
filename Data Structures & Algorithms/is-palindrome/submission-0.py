import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9 \s]', '', s).lower()
        clean = clean.replace(" ", "")
        print(clean)
        left = 0
        right = len(clean) - 1
               
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True




