class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalpha():
                string += i.lower()
            elif i.isdigit():
                string += digit
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - 1 - i]:
                return False
        return True