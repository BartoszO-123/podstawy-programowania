import queue

def convert_to_binary(number):
    stack = queue.LifoQueue()
    original_number = number

    print(f"{'Division':<10} {'Remainder'}")
    
    if number == 0:
        stack.put(0)
    else:
        while number > 0:
            remainder = number % 2
            next_val = number // 2
            print(f"{number:>2} / 2 = {next_val:<4} {remainder}")
            
            stack.put(remainder)
            number = next_val

    binary_str = ""
    while not stack.empty():
        binary_str += str(stack.get())

    print("-" * 25)
    print(f"Natural number: {original_number}")
    print(f"Binary number:  {binary_str}")

convert_to_binary(18)