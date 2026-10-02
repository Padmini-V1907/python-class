def add_waypoint(point, route=None):
    if route is None:
        route = []

    route.append(point)
    return route


route1 = add_waypoint((0, 0))
route2 = add_waypoint((5, 5))

print("route1 =", route1)
print("route2 =", route2)
print("same object?", route1 is route2)