import csv
import sys


def calculateArea(p1, p2, p3):
    """
    Calculates the area of a triangle given its three vertices using Shoelace formula.
    """
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)

def findPossibleTriangles(points):
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
        print("Usage: python <program name> <filename>")
        return
    points = []
    filename = sys.argv[1]
    # read the points from the input file
    with open(filename, "r") as openedFile:
        reader = csv.reader(openedFile)
        next(reader)  # skip header
        for row in reader:
            x, y = map(float, row)  # convert all strings except the header to float
            points.append((x, y))  # add points as tuples

    maxArea = 0  # initialize maximum area to 0
    triangles = findPossibleTriangles(points)
    # calculate the area of each triangle and update the maximum area
    for triangle in triangles:
        currentArea = calculateArea(triangle[0], triangle[1], triangle[2])
        if currentArea > maxArea:
            maxArea = currentArea

    # print the maximum area of a triangle
    print("Maximum area of a triangle: ", maxArea)

if __name__=="__main__":
    main()







