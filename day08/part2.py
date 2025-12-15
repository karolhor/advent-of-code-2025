import sys
import math
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int
    circuit: 'Cirquit'

    def distance(self, other: 'Point') -> float:
        return sum([math.pow(self.x - other.x, 2), math.pow(self.y - other.y, 2),math.pow(self.z - other.z, 2)])

@dataclass
class Circuit:
    points: list[Point]

    def __init__(self, points: list[Point]):
        self.points = points
        for p in points:
            p.circuit = self

    def join(self, other: 'Circuit'):
        self.points.extend(other.points)
        for p in other.points:
            p.circuit = self

@dataclass
class Pair:
    left: Point
    right: Point
    distance: float

def main(input_filename):
    circuits, points = read_input(input_filename)

    pairs = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            pairs.append(Pair(points[i], points[j], points[i].distance(points[j])))

    pairs.sort(key=lambda p: p.distance)

    result = 0
    for pair in pairs:
        if pair.left.circuit == pair.right.circuit:
            continue
        else:
            left_circuit = pair.left.circuit
            pair.right.circuit.join(left_circuit)
            circuits.remove(left_circuit)

        if len(circuits) == 1:
            result = pair.left.x * pair.right.x
            break

    print("The result is:", result)


def read_input(input_filename):
    with open(input_filename) as input_file:
        lines = input_file.readlines()

        coordinates =  [ line.split(',') for line in lines]
        circuits = []
        points = []
        for c in coordinates:
            p = Point(int(c[0]), int(c[1]), int(c[2]), None)
            circuit = Circuit([p])
            circuits.append(circuit)
            points.append(p)
        return (circuits, points)

def _dist(p, q):
   return math.sqrt(math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2) + math.pow(p[2] - q[2], 2))
if __name__ == '__main__':
    main(sys.argv[1])