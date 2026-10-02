# Set of visited grid cells
visited_cells = {(0, 0), (1, 0)}

visited_cells.add((1, 1))
visited_cells.add((0, 0))

print("Visited cells:", visited_cells)
print("Number of cells:", len(visited_cells))
print("(1, 1) visited?", (1, 1) in visited_cells)
print("(8, 8) visited?", (8, 8) in visited_cells)

# Removing duplicate error codes
error_codes = ["W3", "W9", "W3", "W2", "W9"]

print("All codes:", error_codes)
unique_codes = set(error_codes)
print("Unique codes:", unique_codes)
print("Unique count:", len(unique_codes))

# Tuples and unpacking
coordinates = (6.4, 3.9)

print(coordinates, type(coordinates))

horizontal, vertical = coordinates
print("horizontal =", horizontal, "| vertical =", vertical)

one_value = (8,)
print(one_value, type(one_value))

# Robot grid-visit simulation
cells = set()

cells.add((0, 0))
cells.add((0, 1))
cells.add((1, 1))
cells.add((2, 1))
cells.add((2, 2))
cells.add((1, 2))
cells.add((0, 2))
cells.add((2, 2))   # repeated
cells.add((1, 1))   # repeated

print("Visited:", cells)
print("Distinct cells:", len(cells))
print("Was (2, 2) visited?", (2, 2) in cells)