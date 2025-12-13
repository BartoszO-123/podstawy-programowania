speed_limit_min = 40
speed_limit_max = 140


try:
    car_speed = float(input("Enter car speed: "))

    if car_speed < speed_limit_min:
        print("Warning: invalid car speed!!")
        print(
            f"(Speed {car_speed:.0f} km/h is below the minimum limit of {speed_limit_min} km/h.)"
        )

    elif car_speed > speed_limit_max:
        print("Warning: invalid car speed!!")
        print(
            f"(Speed {car_speed:.0f} km/h is above the maximum limit of {speed_limit_max} km/h.)"
        )

    else:
        print("Car speed is valid for the highway.")

except ValueError:
    print("Error: Invalid input. Please enter a numerical value for speed.")
