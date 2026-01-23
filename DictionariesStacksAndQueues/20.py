def hotel_list(hotels):
    # Extracts the "name" from each dictionary and joins them with a comma 
    names = [hotel["name"] for hotel in hotels]
    return ", ".join(names)

def avg_price(hotels):
    # Calculates the average price and rounds it to an integer 
    total_price = sum(hotel["price"] for hotel in hotels)
    average = total_price / len(hotels)
    return int(round(average))

# Data provided for Krakow and Sopot [cite: 2]
hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

# Calculate values for Krakow
krakow_names = hotel_list(hotels_in_Krakow)
krakow_avg = avg_price(hotels_in_Krakow)

# Calculate values for Sopot
sopot_names = hotel_list(hotels_in_Sopot)
sopot_avg = avg_price(hotels_in_Sopot)

# Determine which city is cheaper 
cheaper_city = "Krakow" if krakow_avg < sopot_avg else "Sopot"
if krakow_avg == sopot_avg:
    cheaper_city = "Both cities have the same average price"

# Display results in the required format [cite: 2]
print(f"Hotels in Krakow: {krakow_names}")
print(f"Average hotel price in Krakow: {krakow_avg}")
print(f"Hotels in Sopot: {sopot_names}")
print(f"Average hotel price in Sopot: {sopot_avg}")
print(f"Cheaper hotels in: {cheaper_city}")