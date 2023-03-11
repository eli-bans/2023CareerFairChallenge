import csv
import sys


def calculate_area(p1, p2, p3):
    """
    Calculates the area of a triangle given its three vertices.
    """
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)


def is_convex(p1, p2, p3):
    """
    Checks if three points form a convex polygon.
    """
    cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    return cross_product > 0


def find_safe_polygon(filename):
    # Read in the list of points from the CSV file
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        points = list(map(lambda row: [float(row[0]), float(row[1])], reader))

    # Find the three vertices of the triangle with the largest area
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                area = calculateArea(points[i], points[j], points[k])
                if area > max_area:
                    max_area = area
                    max_points = [points[i], points[j], points[k]]
    """
    
    Check if any additional points can be added to the max_points list to form a larger polygon.
    
    """

    # This is done by checking all possible combinations of three points in the input list 'points',
    # except for the current max_points list. If a combination of three points forms a convex polygon,
    # the area of the polygon is calculated by calling calculateArea function. If the sum of the area of
    # this polygon and the combined area of all other polygons formed by adding a point to it
    # is greater than the current max_area, then the new set of points is assigned as the new max_points.
    # The combined area is calculated by iterating over all points and checking if it is inside the
    # polygon formed by the three points. If it is inside, the area of the triangle formed by the three
    # points and this point is calculated and added to the combined_area variable.
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                # Skip the current max_points list to avoid duplicate calculations
                if [points[i], points[j], points[k]] == max_points:
                    continue
                # Check if this combination of three points forms a convex polygon
                if is_convex(points[i], points[j], points[k]):
                    area = calculate_area(points[i], points[j], points[k])
                    combined_area = 0
                    for p in points:
                        # Skip the three points forming the current polygon
                        if p in [points[i], points[j], points[k]]:
                            continue
                        # Check if the additional point p is inside the polygon formed by the three points
                        if is_convex(points[i], points[j], p) and is_convex(points[j], points[k], p) and is_convex(
                                points[k], points[i], p):
                            # Calculate the area of the triangle formed by the three points and p
                            combined_area += calculateArea(points[i], points[j], p) + \
                                             calculateArea(points[j],points[k],p) + \
                                             calculateArea(points[k], points[i], p)
                    # If the total area of the polygon formed by the three points and all additional points
                    # is greater than the current max_area, update max_area and max_points
                    if area + combined_area > max_area:
                        max_area = area + combined_area
                        max_points = [points[i], points[j], points[k]]
                        # Append all points that form the new polygon to the max_points list
                        for p in points:
                            if p in [points[i], points[j], points[k]]:
                                continue
                            if is_convex(points[i], points[j], p) and is_convex(points[j], points[k], p) and is_convex(
                                    points[k], points[i], p):
                                max_points.append(p)

                        # Sort the vertices in increasing order of x-coordinates then y-coordinates
                        max_points.sort(key=lambda p: (p[0], p[1]))

    # Write the vertices to a CSV file named safepolygon.csv
    with open('safepolygon.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])
        for point in max_points:
            writer.writerow(point)



