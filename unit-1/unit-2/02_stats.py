# Function returning multiple values
def get_stats(numbers):
    average = sum(numbers) / len(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    return average, smallest, largest


readings = [22.5, 23.1, 21.8, 24.0, 22.9]

result = get_stats(readings)
print("as a tuple:", result, type(result))


# Function without return
def greet(robot):
    print("Hello", robot)


answer = greet("Alpha")
print("returned:", answer)
print("type:", type(answer))


# Returning None when division is not possible
def divide(a, b):
    if b == 0:
        return None
    return a / b


print(divide(10, 2))
print(divide(10, 0))


# Modifying a list inside a function
def add_value(data, value):
    data.append(value)


numbers = [10, 20]
add_value(numbers, 30)

print("caller list is now:", numbers)


# Rebinding a local variable
def change_list(data):
    data = [99]
    return data


numbers2 = [10, 20]
change_list(numbers2)

print("caller list unchanged:", numbers2)


# Calculate distance between points
def calculate_distance(points):
    distance = 0

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


distance = calculate_distance([(0, 0), (3, 4)])

print("distance:", distance)

if distance is not None:
    print("usable value:", distance + 1)
else:
    print("cannot use the distance")