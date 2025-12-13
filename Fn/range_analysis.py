def f(x, y):
    count = 0
    # Iteracja od największej do najmniejszej, aby zacząć od największej ujemnej
    for number in range(y - 1, x - 1, -1):
        if number < 0 and number % 2 == 0:
            count += 1
    return count