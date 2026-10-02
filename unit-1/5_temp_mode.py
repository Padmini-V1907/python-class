# Temperature check
temperature = 42.5

if temperature > 40:
    print("Cooling system activated")

print("Temperature check finished")

# Enclosure operating mode
temperature = float(input("Enter enclosure temperature: "))

if temperature < 20:
    operation = "heater on"
elif temperature <= 40:
    operation = "normal"
elif temperature <= 60:
    operation = "cooling"
else:
    operation = "emergency shutdown"

print("Operating mode:", operation)

# Marks evaluation
marks = 88

if marks >= 90:
    result = "DISTINCTION"
elif marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)