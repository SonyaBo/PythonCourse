class Vector:
    x: int
    y: int

    def __init__(self,x: int,y: int)-> None:
        self.x = x
        self.y = y
    def __add__(self, other: "Vector")->"Vector":
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other:"Vector")->"Vector":
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other:"Vector")->"Vector":
        return Vector(self.x * other.x, self.y * other.y)
    def __eq__ (self, other:"Vector")->bool:
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"x: {self.x} y: {self.y}"

v1 = Vector(1,2)
v2 = Vector(3,4)

print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1==v2)
