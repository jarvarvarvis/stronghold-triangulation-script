import math
from helper import *
from visualization import *

# Get input
print("Eye:")
print("============================================================")
first_eye_throw_player_x = float(input("Enter player X: "))
first_eye_throw_player_z = float(input("Enter player Z: "))
first_eye_target_x = float(input("Enter eye X: "))
first_eye_target_z = float(input("Enter eye Z: "))

first_eye_pos = (first_eye_throw_player_x, first_eye_throw_player_z)
first_eye_target = (first_eye_target_x, first_eye_target_z)

# Plot stronghold rings
plot_rings()

point_collection = PointCollection()
point_collection.add_point("Eye", first_eye_pos)
point_collection.add_point("Eye target", first_eye_target)

point_collection.add_line(0, 1)

point_collection.plot()

display("Point finder")
