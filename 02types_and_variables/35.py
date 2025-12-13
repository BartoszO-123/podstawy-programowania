###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input("Enter swift: ")
print(f"Bank Code: {swift[:4]}")
print(f"Country Code: {swift[4:6]}")
