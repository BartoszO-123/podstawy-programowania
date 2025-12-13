vehicle_speed = int(input("Enter vehicle speed:"))
min_speed = 40
max_speed = 140
good_speed = vehicle_speed >= min_speed and vehicle_speed <= max_speed
print(f"Speed is valid:{good_speed}")
