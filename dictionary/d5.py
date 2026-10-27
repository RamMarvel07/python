cities = {
    "Mumbai": 20667656,
    "Delhi": 32941000,
    "Bangalore": 13193000,
    "Chennai": 10971000,
    "Hyderabad": 10268000
}

print("Cities:", list(cities.keys()))
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found.")
