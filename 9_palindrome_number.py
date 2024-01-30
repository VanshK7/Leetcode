class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return (str(x) == str(x)[::-1])

        # Solving it without converting it to a string
        og_x=x
        y=0
        while(x>0):
            y=(y*10) + (x%10)
            x//=10
        return og_x==y