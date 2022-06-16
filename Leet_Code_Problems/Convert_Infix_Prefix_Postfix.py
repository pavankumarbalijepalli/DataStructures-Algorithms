#  A + B * C --> A B C * +
###### TBD ######
#TODO: Implement Infix to Postfix and Infix to Prefix

def infix_postfix(infix: str):
    ops = []
    stack = ['(']
    infix = infix+')'
    post = []
    for i in infix.strip():
        if i in ['+', '-', '*','/']:
            if ops == []:
                ops.append(i)
            # TODO HERE
            else:
                pass
            
        elif i == '(':
            stack.append(i)
        elif i == ')':
            pass
        else:
            post.append(i)

    
    print()

if __name__=='__main__':
    infix_postfix('A+B*C')