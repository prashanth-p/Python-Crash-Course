cars = ["ford", "Audi", "bMw", "mercedes"]
car = "Ford"
i = 0
for car in cars:
    car = car.lower()
    cars[i] = car
    i += 1
print(cars)

if car.lower() in cars:
    print("Boyyah bitches!!")
