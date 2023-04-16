class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #optimized solution
        s = str(x)
        return s == s[::-1]
    

        #My solution
        # s = str(x)
        # r = ""
        # i=len(s)
        # for j in range(i,0,-1):
        #     r = r + s[j-1]
            
        # if(s == r):
        #     return True
        # else:
        #     return False
        
        
