import math
from helper import *

# Get input
# First eye
print("First eye:")
print("============================================================")
first_eye_throw_player_yaw = float(input("Enter player yaw: "))
first_eye_throw_player_x = float(input("Enter player X: "))
first_eye_throw_player_z = float(input("Enter player Z: "))

print()
print("Move between eye throws:")
print("============================================================")
print("Please rotate left/right by ~90°, exact angles:")

exact_yaw_left = wrap_minecraft_yaw_angle(first_eye_throw_player_yaw - 90)
print(f"- Left yaw: {exact_yaw_left}°")

exact_yaw_right = wrap_minecraft_yaw_angle(first_eye_throw_player_yaw + 90)
print(f"- Right yaw: {exact_yaw_right}°")

print()
print("Please move forwards now (I recommend >150 blocks, but moving even further will increase the accuracy)")

# Second eye
print()
print("Second eye:")
print("============================================================")
second_eye_throw_player_yaw = float(input("Enter player yaw: "))
second_eye_throw_player_x = float(input("Enter player X: "))
second_eye_throw_player_z = float(input("Enter player Z: "))

# Calculate distance between the throw locations
throws_vec = (second_eye_throw_player_x - first_eye_throw_player_x, second_eye_throw_player_z - first_eye_throw_player_z)
throws_distance = vector_magnitude(throws_vec)

# Calculate look vectors from yaw values
first_eye_forward = look_vector(first_eye_throw_player_yaw)
second_eye_forward = look_vector(second_eye_throw_player_yaw)

# Calculate angles
alpha_radians = vector_angle(first_eye_forward, throws_vec)
beta_radians = vector_angle(second_eye_forward, throws_vec)

# Calculate height of the triangle
side_d_length = throws_distance * math.sin(alpha_radians) * math.sin(beta_radians) / math.sin(alpha_radians + beta_radians)

# Calculate distance from first throw point to stronghold
stronghold_dist_from_first = side_d_length / math.sin(alpha_radians)

# Calculate the location of the stronghold
stronghold_location_x = first_eye_throw_player_x + first_eye_forward[0] * stronghold_dist_from_first
stronghold_location_z = first_eye_throw_player_z + first_eye_forward[1] * stronghold_dist_from_first
stronghold_location = (stronghold_location_x, stronghold_location_z)

# Output
print()
print("Triangulation data:")
print("============================================================")
print(f"First eye direction: {first_eye_forward}")
print(f"Second eye direction: {second_eye_forward}")
print(f"Moved distance between throws: {throws_distance}")
print()
print(f"Alpha: {alpha_radians} radians")
print(f"Beta: {beta_radians} radians")
print()
print(f"Length of d (height of triangle): {side_d_length}")
print(f"Distance from first point to stronghold: {stronghold_dist_from_first}")
print(f"Forward direction from first point: {first_eye_forward}")
print()
print(f" => Triangulated stronghold location: {stronghold_location}")
