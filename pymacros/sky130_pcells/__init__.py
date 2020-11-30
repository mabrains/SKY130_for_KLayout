########################################################################################################################
## Mabrains Company LLC
##
## Mabrains Pcells Generators for Klayout for Skywaters 130nm
########################################################################################################################

import pya

from .via import ViaGenerator
from .nmos18 import NMOS18
from .circle import Circle

class Sky130(pya.Library):
    """
    The library where we will put the PCell into
    """

    def __init__(self):
        # Set the description
        self.description = "Skywaters 130nm Pcells"

        # Create the PCell declarations
        self.layout().register_pcell("via", ViaGenerator())
        self.layout().register_pcell("nmos18", NMOS18())
        self.layout().register_pcell("Circle", Circle())

        # Register us with the name "MyLib".
        self.register("SKY130")
