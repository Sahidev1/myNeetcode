
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        curr = len(digits) - 1
        tmp = 0
        while curr >= 0:
            tmp = digits[curr] + 1
            digits[curr] = tmp % 10
            if tmp < 10: break

            if curr == 0 and digits[curr] == 0:
                digits.insert(0,1)
                break
            curr -= 1
        return digits

            
