import mesa

from .portrayal import portrayPDAgent
from .model import PdGrid
from mesa.visualization.UserParam import Slider, NumberInput, Checkbox

# Make a world that is 50x50, on a 500x500 display.
canvas_element = mesa.visualization.CanvasGrid(portrayPDAgent, 50, 50, 500, 500)

model_params = {
    "height": 50,
    "width": 50,
    "schedule_type": mesa.visualization.Choice(
        "Scheduler type", value="Random", choices=list(PdGrid.schedule_types.keys())
    ),
    "random_seed": Checkbox("Random Seed", value=False),
    "seed": NumberInput("Random Seed", value=42),
}

server = mesa.visualization.ModularServer(
    PdGrid, [canvas_element], "Prisoner's Dilemma", model_params
)
