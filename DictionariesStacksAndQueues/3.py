# Create an array with 5 dictionaries, each containing a country and its population. Then, print the array contents.

countries = [
    {'name': 'Poland', 'population': 38000000},
    {'name': 'Egypt', 'population': 109300000},
    {'name': 'Vietnam', 'population': 97470000},
    {'name': 'Germany', 'population': 83200000},
    {'name': 'Argentina', 'population': 45810000}
]

print(f'{'COUNTRY':<10} {'POPULATION'}')

for country in countries:
    name = country['name']
    population = country['population']
    print(f'{name:<10} {population}')