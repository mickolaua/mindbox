from figlib.figure import Figure, FigureParams, IncorrectFigureParamsError
import math


class Triangle(Figure):

    id = "triangle"
    name = "Triangle"

    def __assign_params__(self, params: FigureParams):
        self._side_a = params.get("side_a", 0)
        self._side_b = params.get("side_b", 0)
        self._side_c = params.get("side_b", 0)

        if self._side_a == 0 or self._side_b == 0 or self._side_c == 0:
            raise IncorrectFigureParamsError(
                "All sides of the triangle must be greater than zero"
            )

    @property
    def is_right(self) -> bool:
        """Check if the triangle is a right triangle using the Pythagorean theorem."""
        sides = sorted([self._side_a, self._side_b, self._side_c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

    @property
    def area(self) -> float:
        """Calculate area using Heron's formula."""
        semiperimeter = (self._side_a + self._side_b + self._side_c) / 2
        area = math.sqrt(
            semiperimeter
            * (semiperimeter - self._side_a)
            * (semiperimeter - self._side_b)
            * (semiperimeter - self._side_c)
        )
        return area

    def __repr__(self) -> str:
        return f"<Triangle with sides {self._side_a}, {self._side_b}, {self._side_c}>"
