def time_string(hours, minutes, time_format):
    minutes_str = f"{minutes:02d}"

    if time_format == "24":
        return f"{hours:02d}:{minutes_str}"

    elif time_format == "12":
        ampm = "am" if hours < 12 else "pm"

        display_hours = hours % 12
        if display_hours == 0:
            display_hours = 12

        if hours == 12 and ampm == "pm":
            return f"{display_hours}:{minutes_str}"

        return f"{display_hours}:{minutes_str}{ampm}"

    else:
        return "Invalid format"


print(f"(15, 38, '24'): {time_string(15, 38, '24')}")
print(f"(8, 3, '24'): {time_string(8, 3, '24')}")
print(f"(0, 5, '24'): {time_string(0, 5, '24')}")
print(f"(11, 15, '12'): {time_string(11, 15, '12')}")
print(f"(0, 7, '12'): {time_string(0, 7, '12')}")
print(f"(7, 30, '12'): {time_string(7, 30, '12')}")
print(f"(12, 46, '12'): {time_string(12, 46, '12')}")
print(f"(13, 10, '12'): {time_string(13, 10, '12')}")
print(f"(19, 2, '12'): {time_string(19, 2, '12')}")
