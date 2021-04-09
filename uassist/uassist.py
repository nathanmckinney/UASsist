"""Main module."""
import os
import ipyleaflet
from ipyleaflet  import Map, FullScreenControl, LayersControl, DrawControl, MeasureControl, ScaleControl, TileLayer

class Map(ipyleaflet.Map):
    def __init__(self, **kwargs):
        if "center" not in kwargs:
            kwargs["center"] = [40,-100]
            