import csv
import sys


def calculate_area(p1, p2, p3):
    """
    Calculates the area of a triangle given its three vertices using Shoelace formula.
    """
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)

def find_possible_triangles(points):
    """
    Finds all possible triangles that can be formed from the given points.
    """
    triangles=[]
    for i in range(len(points)-2):
        for j in range(i + 1, len(points)-1):
            for k in range(j + 1, len(points)):
                triangle = [points[i], points[j], points[k]]
                triangles.append(triangle)
    return triangles


def main():
    # to make sure user enters appropriate command
    if len(sys.argv) != 2:
        print("Expected <program name> <filename>")
        return
    points = []
    filename = sys.argv[1]
    # read the points from the input file
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            x, y = map(float, row)  # convert all strings except the header to float
            points.append((x, y))  # add points as tuples

    max_area = 0  # initialize maximum area to 0
    triangles = find_possible_triangles(points)
    # calculate the area of each triangle and update the maximum area
    for triangle in triangles:
        current_area = calculate_area(triangle[0], triangle[1], triangle[2])
        if current_area > max_area:
            max_area = current_area
            coordinates = [triangle[0], triangle[1], triangle[2]]

    # print the maximum area of a triangle
    print("Maximum area of a triangle: ", max_area)

    # write the coordinates of the maximum triangle to the file safetriangle.csv
    sorted_coordinates = sorted(coordinates,key=lambda c: (c[0],c[1]))
    with open('safetriangle.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])
        writer.writerows(coordinates)

if __name__=="__main__":
    main()







