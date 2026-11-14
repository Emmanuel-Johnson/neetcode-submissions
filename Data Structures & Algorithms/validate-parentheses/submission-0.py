class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        for i in s:
            if i not in my_dict:
                stack.append(i)
            else:
                if stack and stack[-1] == my_dict[i]:
                    stack.pop()
        if not stack:
            return True
        return False