# Heading wrap-around
direction = 358
rotation = 7

print("Without wrap-around:", direction + rotation)
print("With wrap-around:", (direction + rotation) % 360)
print("Negative angle normalized:", (-45) % 360)

# Comparison and logical operators
travel_distance = 7.5
maximum_distance = 12

print(travel_distance < maximum_distance)
print(travel_distance == maximum_distance)
print(0 <= travel_distance < maximum_distance)

power = 55

print(travel_distance > 5 and power > 30)
print(travel_distance > 5 or power > 90)
print(travel_distance > 5)

# Robot movement safety
"""
The robot is safe to move only when:
distance > 10
battery > 20
robot is NOT docked
"""

distance = 25
battery = 65
docked = False

print(distance > 10 and battery > 20 and not docked)