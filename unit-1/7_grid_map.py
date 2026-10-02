# Waypoint navigation
route = [(1, 1), (3, 4), (6, 2)]

for point in route:
    print("Moving toward:", point)

# Loop ranges
for step in range(4):
    print("Checking", step)

print("---")

for number in range(2, 8):
    print(number, end=" ")

print()

for countdown in range(12, 1, -3):
    print(countdown, end=" ")

print()

# Accumulating sensor readings
measurements = [18.4, 21.7, 19.9, 23.5, 20.6]

total_reading = 0

for value in measurements:
    total_reading += value

print(f"Total: {total_reading:.2f}")
print("Number of readings:", len(measurements))
print(f"Average: {total_reading / len(measurements):.2f}")

# Nested loops - obstacle map
blocked = [(1, 3), (2, 2), (4, 0)]

for x in range(5):
    for y in range(5):
        symbol = "#" if (x, y) in blocked else "."
        print(symbol, end="")
    print()

# 8x8 grid with start, goal and obstacles
blocked_cells = [(2, 4), (4, 6), (6, 1), (3, 5)]

for row in range(8):
    for column in range(8):
        position = (row, column)

        if position == (0, 0):
            marker = "S"
        elif position == (7, 7):
            marker = "G"
        elif position in blocked_cells:
            marker = "X"
        else:
            marker = "."

        print(marker, end=" ")
    print()

# Continue and break
sensor_values = [18, -5, 42, 75, 29]

for value in sensor_values:
    if value < 0:
        continue

    if value > 70:
        print("Danger detected:", value)
        break

    print("Reading safe:", value)