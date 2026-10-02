# Battery input
battery_level = int(input("Battery percentage: "))
print("After charging:", battery_level + 10)

# Robot information and formatting
robot = "Nova"
charge_level = 83.729

print("Robot:", robot, "| Battery:", charge_level, "%")
print(f"{robot} battery level: {charge_level}%")
print(f"{robot} battery level: {charge_level:.1f}%")
print(f"{robot:<10} | {charge_level:>6.2f}%")

# Runtime calculation
capacity_mAh = float(input("Enter battery capacity in mAh: "))
current_mA = float(input("Enter current consumption in mA: "))

if current_mA > 0:
    hours = capacity_mAh / current_mA
    print(f"Estimated runtime: {hours:.2f} hours")
else:
    print("Current consumption must be greater than zero")