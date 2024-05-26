import re
def simplifyPath(self, path: str) -> str:
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)


if __name__=="__main__":
    simplifyPath("/home/")

