import math

number = int(input("Ener number of sides of polygon: "))
length = eval(input("Enter length of side: "))
angle = 360/number


def plot_points(origin, theta, magnitude):
    return (origin[0] + math.cos(theta*math.pi/180)*magnitude, \
            origin[1] + math.sin(theta*math.pi/180)*magnitude)


def find_midpoint(vertices, n):
    return (sum([x[0] for x in vertices])/n, sum([x[1] for x in vertices])/n)


def find_distance(x1y1, x2y2):
    return math.sqrt((x2y2[0] - x1y1[0])**2 + (x2y2[1] - x1y1[1])**2)


points = [(0,0)]
initial = (0, 0)

for i in range(number):
    initial = plot_points(initial, angle*i, length)
    points.append(initial)

midpoint = find_midpoint(points, len(points) - 1)
side_midpoint = find_midpoint(points[0:2], 2)

area = (length * find_distance(midpoint, side_midpoint) * number)/2
print(f"Area of polygon = {area}")