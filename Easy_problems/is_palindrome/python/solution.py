class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(self._isAlphaNumeric, s))
        s = "".join(s).lower()

        strLen = len(s)
        bPtr = 0
        tPtr = strLen - 1
        pMoves = 0


        while pMoves < strLen:
            if s[bPtr + pMoves] != s[tPtr - pMoves]: 
                return False
            pMoves += 1
        return True
    
    def _isAlphaNumeric(self, letter: str)->bool:
        return letter.isalnum()
