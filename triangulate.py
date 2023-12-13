import math

def wrap_minecraft_yaw_angle(angle):
    while angle < -180:
        angle += 360

    while angle > 180:
        angle -= 360

    return angle

def rotate_vector(vector, angle_radians):
    (x, y) = vector
    x_2 = math.cos(angle_radians) * x - math.sin(angle_radians) * y
    y_2 = math.sin(angle_radians) * x + math.cos(angle_radians) * y

    return (x_2, y_2)

# Get input
# First eye
print("First eye:")
print("============================================================")
first_eye_throw_player_yaw = float(input("Enter player yaw: "))
first_eye_throw_player_x = float(input("Enter player X: "))
first_eye_throw_player_z = float(input("Enter player Z: "))

print("Please do not move!")

print()
print("Move between eye throws:")
print("============================================================")
print("Please rotate left/right by ~90°")

optimal_yaw_left = wrap_minecraft_yaw_angle(first_eye_throw_player_yaw - 90)
print(f" -> Optimal left yaw: {optimal_yaw_left}°")

optimal_yaw_right = wrap_minecraft_yaw_angle(first_eye_throw_player_yaw + 90)
print(f" -> Optimal right yaw: {optimal_yaw_right}°")

next_yaw_after_first_eye = float(input("Enter yaw of new movement direction: "))
print("Please move forwards now (I recommend around ~100 blocks, but moving further may increase the accuracy)")
print("Note: Try to keep your camera steady (so that the yaw value does not change)")

# Second eye
print()
print("Second eye:")
print("============================================================")
second_eye_throw_player_yaw = float(input("Enter player yaw: "))
second_eye_throw_player_x = float(input("Enter player X: "))
second_eye_throw_player_z = float(input("Enter player Z: "))

# Calculate distance between the throw locations
throws_dx = second_eye_throw_player_x - first_eye_throw_player_x
throws_dz = second_eye_throw_player_z - first_eye_throw_player_z

throws_distance = math.sqrt(throws_dx * throws_dx + throws_dz * throws_dz)

# Calculate angles
alpha = wrap_minecraft_yaw_angle(next_yaw_after_first_eye - first_eye_throw_player_yaw)
beta = wrap_minecraft_yaw_angle(second_eye_throw_player_yaw - next_yaw_after_first_eye)

alpha_radians = math.radians(alpha)
beta_radians = math.radians(beta)

# Calculate height of the triangle
side_d_length = throws_distance * math.sin(alpha_radians) * math.sin(beta_radians) / math.sin(alpha_radians + beta_radians)

# Calculate distance from first throw point to stronghold
stronghold_dist_from_first = side_d_length / math.sin(alpha_radians)

# Calculate the location of the stronghold
vector_12_x = throws_dx / throws_distance
vector_12_z = throws_dz / throws_distance
forward_from_first = rotate_vector((vector_12_x, vector_12_z), -alpha_radians)

stronghold_location_x = first_eye_throw_player_x + forward_from_first[0] * stronghold_dist_from_first
stronghold_location_z = first_eye_throw_player_z + forward_from_first[1] * stronghold_dist_from_first
stronghold_location = (stronghold_location_x, stronghold_location_z)

# Output
print()
print("Triangulation data:")
print("============================================================")
print(f"Alpha: {alpha}°")
print(f"Beta: {beta}°")
print(f"Moved distance between throws: {throws_distance}")
print(f"length of d (height of triangle): {side_d_length}")
print(f"Distance from first point to stronghold: {stronghold_dist_from_first}")
print(f"Forward direction from first point: {forward_from_first}")
print(f"\n -> Triangulated stronghold location: {stronghold_location}")
