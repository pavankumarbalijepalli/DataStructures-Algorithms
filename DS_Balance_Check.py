def balcheck(s):
    if len(s) % 2 != 0:
        return False

    opening = set('({[')

    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    stack = []
    for p in s:
        if p in opening:
            stack.append(p)

        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, p) not in matches:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    print(balcheck('{[()]}'))
    print(balcheck('{[(()]}'))
