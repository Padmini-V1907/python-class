# List operations
alerts = ["W3", "W8"]
print("Initial:", alerts)

alerts.append("W5")
print("After append:", alerts)

alerts.insert(1, "W1")
print("After insert:", alerts)

alerts.remove("W8")
print("After remove:", alerts)

# References and copies
original = [4, 5, 6]
reference = original
duplicate = original.copy()

reference.append(7)
duplicate.append(100)

print("original =", original)
print("reference =", reference)
print("duplicate =", duplicate)

print("reference is original:", reference is original)
print("duplicate is original:", duplicate is original)

# Removing invalid readings
sensor_data = [25, -1, 40, -1, 55]

valid_data = [value for value in sensor_data if value != -1]
print("Valid readings:", valid_data)

# List comprehensions
values = [8, 19, 42, 27, 63]

scaled_values = [value * 3 for value in values]
high_values = [value for value in values if value >= 30]

print("Scaled:", scaled_values)
print("High readings:", high_values)