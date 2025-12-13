bulbs_on = 0


s1_input = input("Enter state for Switch 1 (1=ON, 0=OFF): ")
light_switch1 = s1_input == "1"


s2_input = input("Enter state for Switch 2 (1=ON, 0=OFF): ")
light_switch2 = s2_input == "1"


if light_switch1:
    bulbs_on += 1


if light_switch2:
    bulbs_on += 2


print(f"\nTotal bulbs lit: {bulbs_on}")
