

def input_string(message):
    return input(message)

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
 
    user_input = input(message).lower()
    return user_input == 'y'