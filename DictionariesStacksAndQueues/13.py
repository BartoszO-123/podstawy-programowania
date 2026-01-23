import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue() 

    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.put(char)
        elif char in ")}]":
            if stack.empty():
                return False 

            last_open = stack.get()
            if last_open != pairs[char]:
                return False 

    return stack.empty() #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
    print(f"Expression 1: {expression1} -> Brackets OK")
else:
    print(f"Expression 1: {expression1} -> Brackets NOT correct")

if brackets_ok(expression2):
    print(f"Expression 2: {expression2} -> Brackets OK")
else:
    print(f"Expression 2: {expression2} -> Brackets NOT correct")

if brackets_ok(expression3):
    print(f"Expression 3: {expression3} -> Brackets OK")
else:
    print(f"Expression 3: {expression3} -> Brackets NOT correct")