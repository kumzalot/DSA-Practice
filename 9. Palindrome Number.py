class Solution: #without conversion to str
    def isPalindrome(self, x: int) -> bool:
        dup = abs(x) #tackling signs
        revNum = 0

        while dup>0:
            ld = dup % 10
            revNum = revNum*10 + ld
            dup = dup//10
        
        return revNum == x
