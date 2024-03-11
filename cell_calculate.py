import json

# Calculate Area  Window
def calculate_window_area(cell):
    frame_area = (cell["frame"]["width"] * cell["frame"]["hight"]) - (cell["frame"]["profile"]["width"] * cell["frame"]["profile"]["depth"])
    glass_area = cell["glas"]["width"] * cell["glas"]["hight"]
    return frame_area + glass_area

# Grid
def calculate_total_window_area(grid):
    total_area = 0

    for cell in grid["cells"]:
        total_area += calculate_window_area(cell)

    return total_area


with open("pfad/datei.json", "r") as file:
    grid_data = json.load(file)

# Constants
window_area = calculate_total_window_area(grid_data)
heat_transfer_coefficient = 0.8 #example

# Calculate Heat transfer
total_heat_transfer = window_area * heat_transfer_coefficient

print("Total Window Area:", window_area)
print("Total Heat Transfer:", total_heat_transfer)


