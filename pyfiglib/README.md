# <b>figlib</b> is a library for mathematics on figures.

# Installation

## Prerequesites

- git
- python >=3.8
- venv

Follow the steps to install the library (NOTE: custom plugins MUST BE added BEFORE INSTALLATION):

1. Clone the repository using command: ```git clone https://github.com/mickolaua/mindbox.git```
2. cd into pyfiglib subfolder with command: ```cd ./pyfiglib```
3. create a virtual environment using command: ```python -m venv .venv``` and activate it with ```./.venv/bin/activate``` (UNIX), or ```.\.venv\Scripts\activate``` on Windows

# Plugins

User must specify Figure plugins before installation. The plugin folder is ```./pyfiglib/figlib/plugins```. A custom plugin must derived from class ```figlib.figure.Figure```. Its API is as follows:

```id: str``` -- unique string indetifier of the plugin needed for its sussesful and loading

```name: str``` -- string description of the plugin

```__assign_params__(self, params: FigureParams)``` -- member function needed for parsing and assigning parameters, should modify the plugin instance in-place. The params is actually a typed dict, where each keyword is an attribute name (it is up to developer to decide whether to assign these attributes to the instance or just use them temporarily). 

```create(params: FigureParams)``` -- member function, which actually triggers parsing and assigning of the parameters. it has the same signature for all plugins. It must be called after plugin instance created.

```area: float``` -- property which returns the area of the figure.


Here is the example of what a custom plugin should have looked based on standard ```Circle``` plugin:

```
class Circle(Figure):
    id = "circle"
    name = "Circle"

    def __assign_params__(self, params: FigureParams):
        self._radius = params.get("radius", 0)

    @property
    def radius(self) -> float:
        try:
            return self._radius
        except AttributeError as e:
            raise IncorrectFigureParamsError(
                "Possibly no radius attribute was specified at the object creation"
            ) from e

    @property
    def area(self) -> float:
        return math.pi * self.radius**2

    def __repr__(self) -> str:
        return f"<Circle with radius={self.radius}>"
```

Now one can store it under path ```./pyfiglib/figlib/plugins/custom_plugin.py``` and use it from code as is follows:

```
from figlib.figure import get_figure_by_id
circle = get_figure_by_id("circle", {"radius": 10})
print("Radius:", circle.radius, "Area:", circle.area)
```
