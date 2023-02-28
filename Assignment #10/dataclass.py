from dataclasses import dataclass
import typing

@dataclass
class Point:
    x: float
    y: float
    z: float

@dataclass
class PointObject():
    name: str
    # coordinates: typing.Tuple[Point]
    coordinates: Point(x=float, y=float, z=float)
    # coordinates: (float, float, float)

point_1 = PointObject("fdfd", (12.34, 434.545, 343.54))
print(point_1)
