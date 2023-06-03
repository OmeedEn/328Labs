
#Omeed Enshaie
def isValid(s: str) -> bool:
    arr = []
    open = '({['
    close = ')]}'

    for char in s:
        if char in open:
            arr.append(char)
        elif char in close:
            if not arr:
                return False
            if char == ')' and arr[-1] != '(':
                return False
            if char == ']' and arr[-1] != '[':
                return False
            if char == '}' and arr[-1] != '{':
                return False
            arr.pop()
    return not arr



