import pytest
from figlib.figure import load_plugins


def test():
    figs = load_plugins()
    assert len(figs) == 2, "Must be 2 figure plugins"


if __name__ == "__main__":
    test()