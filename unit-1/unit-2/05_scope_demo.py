# Local variable
total = 0

def increase():
    value = 0
    value += 1
    return value

print(increase(), increase(), total)


# Global constant
LIMIT = 70

def check_alert(value):
    return value > LIMIT

print(check_alert(85), check_alert(60))


# Local variable cannot modify the global one
total = 0

def increase():
    total += 1
    return total

# increase() would give an error because total is local here.


# Using global
total = 0

def increase():
    global total
    total += 1
    return total

print(increase(), increase(), increase())
print("global total is now:", total)


# Passing values instead of using global
def increase(value):
    return value + 1

total = 0
total = increase(total)
total = increase(total)

print("total:", total)


# Local list
def create_report():
    report = ["header"]
    report.append("body")
    return len(report)

print(create_report())
print(create_report())

print("report" in dir())