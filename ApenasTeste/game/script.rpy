# parte_Atributos
default knowledge = 1
default charm = 2
default guts = 3
default kindness = 4
default proficiency = 5


define e = Character("Eileen")

# parte_inventário

default inventory = []
default selected item = None
default pc = Player(7, 5, 5, 3, 2, 1)

default sword_item = Weapon("sword", 10, 5, "sword")
default pie_item = Consumable("pie", 50, 100, 0)
default cauldron_item = KeyItem("cauldron")
default shield_item = Armor("armor shield", 15, 5, 4, "shield")


label start:
    scene ruas

    # parte_inventário
    $inventory.append(sword_item)
    $inventory.append(pie_item)
    $inventory.append(cauldron_item)
    $inventory.append(shield_item)
    

    show screen gameUI
    "Test"