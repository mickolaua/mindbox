import pytest


def test():
    from figlib.figure import get_figure_by_id
    circle = get_figure_by_id("circle", {"radius": 10})
    print(circle)
    assert circle is not None, "Circle must be found"
    print("Radius:", circle.radius, "Area:", circle.area)
    assert circle.area == pytest.approx(314.1592653589793), "Circle area must be correct"


if __name__ == "__main__":
    test()