class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {"}" : "{", "]" : "[", ")" : "("}
        for i in s:
            if i not in my_dict:
                stack.append(i)
            else:
                if stack and stack[-1] == my_dict[i]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False