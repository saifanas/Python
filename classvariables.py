from car import Car


car_1 = Car("Chevy", "Corvette", "2022", "Blue")
car_2 = Car("Ford", "Mustang", "2023", "Red")

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)