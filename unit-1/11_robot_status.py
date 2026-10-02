# Robot dictionary
robot = {
    "name": "Nova",
    "battery": 85,
    "mode": "manual"
}

print(robot)
print(robot["name"])

robot["battery"] = robot["battery"] - 10
robot["speed"] = 0.5

print(robot)

print("keys :", list(robot.keys()))
print("values:", list(robot.values()))


# Checking a missing key
robot = {
    "name": "Nova",
    "battery": 75
}

print(robot.get("speed"))
print(robot.get("speed", 0.0))
print("speed" in robot)


# Counting error codes
errors = ["E1", "E3", "E1", "E2", "E3", "E1"]

count = {}

for error in errors:
    count[error] = count.get(error, 0) + 1

print(count)

for error in sorted(count, key=count.get):
    print(f"{error} occurred {count[error]} time(s)")


# Counting letters in a name
name = "shubham"
letters = {}

for letter in name:
    letters[letter] = letters.get(letter, 0) + 1

print(letters)

for letter in sorted(letters, key=letters.get, reverse=True):
    print(f"{letter} occurred {letters[letter]} time(s)")