country_names = input().split(", ")
capital_cities = input().split(", ")

country_capitals = {country_names[i]: capital_cities[i] for i in range(len(country_names))}

for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")