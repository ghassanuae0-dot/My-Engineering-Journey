car_name = input("Enter car model name: ")
weight_text = input("Enter car weight in kg: ")
speed_text = input("Enter car speed in km/h: ")

weight_number = int(weight_text)
speed_number = int(speed_text)

momentum = weight_number * speed_number

print("Car Model: " + car_name)
print("Car Momentum Score: " + str(momentum) + " kg.km/h")