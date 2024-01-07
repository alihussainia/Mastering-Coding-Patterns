class Solution:
    def isPalindrome(self, x: int) -> bool:
        left=0
        x=str(x)
        right=len(x)-1

        while left < right:

            if x[left] != x[right]:
                return False
            
            else:
                left+=1
                right-=1
        
        return True
