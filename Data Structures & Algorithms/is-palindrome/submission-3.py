class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #lower all letters for easier check
        s = s.casefold()


        #check if any alphabetical char in string
        if not any(char.isalnum() for char in s):
            return True


        #move pointers to outer letters and initial check
        left = 0
        right = len(s) - 1

        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1
        
        if s[left] != s[right]:
                return False


        #check each pair of valid char on each end of string until pointers meet
        #if reach end of loop, isPalidrome is true
        while left < right:
            if s[left] != s[right]:
                return False
            
            #increment left and right until valid char
            left += 1
            while not s[left].isalnum():
                left += 1

            right -= 1
            while not s[right].isalnum():
                right -= 1

        return True