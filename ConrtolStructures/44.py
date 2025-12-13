try:
    x_input = input("Enter x coordinate: ")
    x = float(x_input)
    y_input = input("Enter y coordinate: ")
    y = float(y_input)

except ValueError:
    print("Error: Invalid input. Coordinates must be numerical values.")

    x = None
    y = None


location_message = ""

if x is not None and y is not None:
    if x == 0 and y == 0:
        location_message = "Point P(0,0) is at the origin of the coordinate system."

    elif x == 0:
        location_message = f"Point P({x_input},{y_input}) is located on the Y-axis."
    elif y == 0:
        location_message = f"Point P({x_input},{y_input}) is located on the X-axis."

    elif x > 0 and y > 0:
        location_message = f"Point P({x_input},{y_input}) is in the first quadrant of the coordinate system."

    elif x < 0 and y > 0:
        location_message = f"Point P({x_input},{y_input}) is in the second quadrant of the coordinate system."

    elif x < 0 and y < 0:
        location_message = f"Point P({x_input},{y_input}) is in the third quadrant of the coordinate system."

    elif x > 0 and y < 0:
        location_message = f"Point P({x_input},{y_input}) is in the fourth quadrant of the coordinate system."

    print(location_message)
