cities = ["Bangalore", "Mysore", "Bellary", "Kerala","Delhi"]
for city in cities:
    print(city)

for i in range(1,10):
    print(i, end=" ")

print(next)

name = "Karnataka"
for letter in name:
    print(letter, end=" ")

for i in range(1,6):
    for j in range(1,6):
        print(f"{i}X{j} = {i*j}")
    print()

cities = ["Bangalore", "Mysore", "Bellary", "Kerala","Delhi"]
for city in cities:
    if city == "Bellary":
        print(f"found{city}!")
        break
    print(city)

cities = ["Bangalore", "Mysore", "Bellary", "Kerala","Delhi"]
for index, city in enumerate(cities):
    print(f"city {index + 1}: {city}")
for city in cities:
    print(city)
else:
    print("No more cities!")


laddus = 4
friends = ["Rahul","Kumar","Apoorva","Geetha","Raju"]
for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
    laddus -= 1
else:
    print("No laddus left")


    