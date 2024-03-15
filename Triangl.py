from Figure import Figure
import turtle
from math import sin, cos, radians

class Triangle(Figure):

    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)


    def draw(self):
        v1 = self.calc_abs_pos(self._vertex1)
        v2 = self.calc_abs_pos(self._vertex2)
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)

if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    triangle.draw()
    turtle.clear()
    for degree in range(3, 363, 3):
        triangle.set_rotation_degree(degree)
        triangle.draw()
        turtle.clear()
    turtle.mainloop()