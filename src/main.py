from characters import *
from equipments import EquipmentSlot
from equipments.runes import DamageRune

from settings.preferences import Preferences


if __name__ == '__main__':
    
    name = input("Username: ")

    Preferences.get_instance().set("name", name)
    
    our_knight = Knight()
    our_knight.set_name(Preferences.get_instance().get("name"))
    our_knight.equip(EquipmentSlot.RIGHT_HAND, "Dagger")

    print(Preferences.get_instance().get("name") + ", travels across countries to live an adventures life...")

    evil_goblin = Goblin()
    evil_goblin.equip(EquipmentSlot.TWO_HAND, "Club")

    print("Then suddenly a " + evil_goblin.get_type() + " appears.")
    print("And attacks " + Preferences.get_instance().get("name"))

    evil_goblin.hit(our_knight)

    print(Preferences.get_instance().get("name") + " tries to fight back")

    our_knight.hit(evil_goblin)

    print("But he couldn't inflict much damage")
    print("then he saw a sword on the ground and grabs it")

    our_knight.unequip(EquipmentSlot.RIGHT_HAND)
    our_knight.equip(EquipmentSlot.RIGHT_HAND, "Sword")

    print("And fearlessly attacks " + evil_goblin.get_type())

    our_knight.hit(evil_goblin)

    print()
    print("After defeating " + evil_goblin.get_type())
    print(Preferences.get_instance().get("name") + " stops at the blacksmith to upgrade his sword")
    print("Then buys three damage rune and goes to training ground to test them")
    print()

    dummy = Dummy()

    # Decorator usage
    our_knight.update_equipment(DamageRune(our_knight.get_weapon()))
    our_knight.hit(dummy)
    our_knight.update_equipment(DamageRune(our_knight.get_weapon()))
    our_knight.hit(dummy)
    our_knight.update_equipment(DamageRune(our_knight.get_weapon()))
    our_knight.hit(dummy)

    print()
    print("After testing his new sword returns to the blacksmith to get his helmet back from repair")
    print("It was finished and he immediately tries it to see how it was done")

    our_knight.equip(EquipmentSlot.HEAD, "Helmet")
