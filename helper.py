import math

def wrap_minecraft_yaw_angle(angle):
    while angle < -180:
        angle += 360

    while angle > 180:
        angle -= 360

    return angle

def look_vector(yaw):
    x = -math.sin(math.radians(yaw))
    y = math.cos(math.radians(yaw))

    # Vector always has a length of 1!
    return (x, y)

def vector_dot(first, second):
    (x1, y1) = first
    (x2, y2) = second

    return x1 * x2 + y1 * y2

def vector_magnitude(vector):
    (x, y) = vector
    return math.sqrt(x * x + y * y)

def vector_angle(first, second):
    numerator = vector_dot(first, second)
    denominator = vector_magnitude(first) * vector_magnitude(second)

    if denominator == 0.0:
        return 0.0

    angle = math.acos(numerator / denominator)

    # Angle >= 180°
    if angle >= math.pi / 2.0:
        angle = math.pi - angle
    return angle

