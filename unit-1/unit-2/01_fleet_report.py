# Battery status
alpha = 12
beta = 28
gamma = 65

def check_battery(name, battery):
    if battery < 15:
        print(f"{name}: CRITICAL")
    elif battery < 30:
        print(f"{name}: LOW")
    else:
        print(f"{name}: OK")

check_battery("Alpha", alpha)
check_battery("Beta", beta)
check_battery("Gamma", gamma)


# Function with default argument
def battery_status(battery, name="Robot"):
    if battery < 15:
        print(f"{name}: CRITICAL")
    elif battery < 30:
        print(f"{name}: LOW")
    else:
        print(f"{name}: OK")

battery_status(10, "Alpha")
battery_status(25, "Beta")
battery_status(70)


# Function returning a value
def battery_band(battery):
    if battery < 15:
        return "critical"
    elif battery < 30:
        return "low"
    else:
        return "OK"


fleet = {
    "Alpha": 12,
    "Beta": 28,
    "Gamma": 65,
    "Delta": 45
}

for name, battery in fleet.items():
    print(f"{name:<7} {battery:>3}% {battery_band(battery)}")


# Return value vs print
def circle_area(radius):
    return 3.14 * radius * radius

area1 = circle_area(2)
area2 = circle_area(3)

print("Total area:", area1 + area2)


# Function with default speed
def move_robot(x, y, speed=1.0):
    print(f"Moving to ({x}, {y}) at {speed} m/s")

move_robot(4, 6)
move_robot(4, 6, 0.5)
move_robot(y=6, x=4)
move_robot(4, speed=2.0, y=6)


# *args and **kwargs
def show_data(*values, **options):
    print("values:", values)
    print("options:", options)

show_data("start")
show_data("point", 4, 6.5)
show_data("warning", level="high", retries=3)
show_data()


# Default list argument
def add_point(point, route=[]):
    route.append(point)
    return route

first_route = add_point((1, 1))
second_route = add_point((4, 4))

print("first route:", first_route)
print("second route:", second_route)
print("same object?", first_route is second_route)