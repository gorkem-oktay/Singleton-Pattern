from ..i_equipment_factory import IEquipmentFactory
from .gauntlet import Gauntlet
from .greave import Greave
from .cuirass import Cuirass
from .helmet import Helmet
from .pauldron import Pauldron


class ArmorFactory(IEquipmentFactory):

    # Factory Method
    def get_equipment(self, name):
        if name == "Helmet":
            return Helmet()
        elif name == "Cuirass":
            return Cuirass()
        elif name == "Pauldron":
            return Pauldron()
        elif name == "Gauntlet":
            return Gauntlet()
        elif name == "Greave":
            return Greave()
        else:
            return None
