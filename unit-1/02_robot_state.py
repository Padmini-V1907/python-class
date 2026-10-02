# Robot information
model = "Orion-X"
charge = 82.5
connected = True
missions = 14

print("Robot:", model)
print("Charge:", charge, "%")
print("Connected:", connected)
print("Missions:", missions)

# Battery updates
remaining_power = 90
print("Initial power:", remaining_power)

remaining_power -= 20
print("After first task:", remaining_power)

remaining_power -= 10
print("After second task:", remaining_power)

# Battery warning
current_charge = 38

if current_charge < 50:
    print("Warning: battery level is low")
    print("Robot should return to the charging station")

print("Robot status check completed")