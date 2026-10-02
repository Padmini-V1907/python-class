import sensors

readings = [62, 84, 71]

print("threshold:", sensors.THRESHOLD)
print("average:", sensors.average(readings))

for reading in readings:
    status = "ALERT" if sensors.is_alert(reading) else "ok"
    print(reading, "->", status)

print("__name__ inside main.py is:", __name__)
print("__name__ inside sensors.py is:", sensors.__name__)

from sensors import is_alert
import sensors as sn

print(sensors.is_alert(85))
print(is_alert(85))
print(sn.is_alert(85))

from sensors import *

THRESHOLD = 30.0

print("my THRESHOLD is", THRESHOLD)
print("is_alert(50) says", is_alert(50))