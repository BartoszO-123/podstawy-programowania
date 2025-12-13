def f(name):
    acronym = ""
    for word in name.split():
        acronym += word[0].upper()
    return acronym


print(f'f("Internet of Things") returns "{f("Internet of Things")}"')
print(f'f("For Your Information") returns "{f("For Your Information")}"')
print(f'f("Python") returns "{f("Python")}"')
print(f'f("random access memory") returns "{f("random access memory")}"')
