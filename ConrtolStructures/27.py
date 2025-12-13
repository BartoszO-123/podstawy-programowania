import time


while True:
    try:
        countdown = int(input("Enter the number of seconds to count down: "))
        if countdown < 1:
            print("Enter a positive number: ")
            continue
        break
    except ValueError:
        print("Invalid value")


word_map = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

print(f"Starting countdown from {countdown} seconds...")

while countdown > 0:
    if countdown <= 5:
        print(word_map[countdown])
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)

print("Time's up!")
