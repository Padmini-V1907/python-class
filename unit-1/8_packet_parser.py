# String formatting and cleanup
robot_name = "  Nova Scout  "

print(f"<{robot_name}>")
print(f"<{robot_name.strip()}>")
print(robot_name.strip().lower())
print(robot_name.strip().upper())
print(robot_name.strip().replace(" ", "-"))
print("Nova" in robot_name)

# Parsing a sensor packet
message = "TEMP=28.5|HUM=64|POWER=82"

entries = message.split("|")

for entry in entries:
    label, reading = entry.split("=")
    print(label, "=>", float(reading))

# Custom robot telemetry packet
telemetry = "GPS=12.5,45.8|MOTOR=0.72|VOLTAGE=11.8"

parts = telemetry.split("|")

for part in parts:
    label, data = part.split("=")

    if label == "GPS":
        coordinates = data.split(",")
        print("GPS latitude:", float(coordinates[0]))
        print("GPS longitude:", float(coordinates[1]))
    else:
        print(label, "=>", float(data))