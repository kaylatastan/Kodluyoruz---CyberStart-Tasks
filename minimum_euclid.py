import math


def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

points = []

for i in range(2):
    x = float(input(f"Nokta {i + 1} için x koordinatını girin: "))
    y = float(input(f"Nokta {i + 1} için y koordinatını girin: "))
    points.append((x, y))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


if distances:
    min_distance = min(distances)
    print(f"Minimum uzaklık: {min_distance}")
else:
    print("Mesafeleri hesaplamak için yeterli nokta yok.")
2
