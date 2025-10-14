from figlib.figure import Figure, FigureParams
import math


class Circle(Figure):

    def __assign_params__(self, params: FigureParams):
        self._radius = params.get("radius", 0)

    @property
    def radius(self) -> float:
        try:
            return self._radius
        except AttributeError as e:
            raise AttributeError(
                "Possibly no radius attribute was specified at the object creation"
            ) from e

    @property
    def area(self) -> float:
        return math.pi * self.radius**2

    def __repr__(self) -> str:
        return f"<Circle with radius={self.radius}>"
