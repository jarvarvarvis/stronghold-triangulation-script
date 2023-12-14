import math
from helper import *
from visualization import visualize_results

# Get input
# First eye
print("First eye:")
print("============================================================")
first_eye_throw_player_x = float(input("Enter player X: "))
first_eye_throw_player_z = float(input("Enter player Z: "))
first_eye_target_x = float(input("Enter eye X: "))
first_eye_target_z = float(input("Enter eye Z: "))

# Second eye
print()
print("Second eye:")
print("============================================================")
second_eye_throw_player_x = float(input("Enter player X: "))
second_eye_throw_player_z = float(input("Enter player Z: "))
second_eye_target_x = float(input("Enter eye X: "))
second_eye_target_z = float(input("Enter eye Z: "))

# Calculate line intersection point
first_eye_pos = (first_eye_throw_player_x, first_eye_throw_player_z)
first_eye_target = (first_eye_target_x, first_eye_target_z)
second_eye_pos = (second_eye_throw_player_x, second_eye_throw_player_z)
second_eye_target = (second_eye_target_x, second_eye_target_z)

L1 = line(first_eye_pos, first_eye_target)
L2 = line(second_eye_pos, second_eye_target)
stronghold_location = find_line_intersection(L1, L2)

# Output
print()
print("Triangulation result:")
print("============================================================")

print(f"First eye position:         {p0}")
print(f"First eye target position:  {p1}")
print(f"Second eye position:        {p2}")
print(f"Second eye target position: {p3}")
print()

distance_between_throw_positions = vector_magnitude((p0[0] - p2[0], p0[1] - p2[1]))
print(f"Distance between throws: {distance_between_throw_positions}")
print()
print(f" => Triangulated stronghold location: {stronghold_location}")

# Visualization
print()
print("Visualization:")
print("============================================================")
print("Note about the results:")
print("If the final stronghold position does *not* lie within a purple ring, the result is probably wrong.")
print("What might have happened is that the positions from which you have thrown the eyes were too close")
print("to each other. Try to run the program again to maybe get more accurate results.")

visualize_results(first_eye_pos, first_eye_target, second_eye_pos, second_eye_target, stronghold_location)
