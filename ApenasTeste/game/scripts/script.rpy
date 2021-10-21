
define e = Character("Eileen")

# parte_inventário

default inventory = []
default selected_item = None
default pc = Player(7, 5, 5, 1)

default arma1_item = Consumable("arma1", 50, 100, 0)
default arma2_item = Consumable("arma2", 50, 100, 0)
default arma3_item = Consumable("arma3", 50, 100, 0)
default faca_item = KeyItem("faca")
default escudo_item = KeyItem("escudo")
default espada_item = KeyItem("espada")


label start:
    scene ruas

    # parte_inventário
    $inventory.append(arma1_item)
    $inventory.append(arma2_item)
    $inventory.append(arma3_item)
    $inventory.append(faca_item)
    $inventory.append(escudo_item)
    $inventory.append(espada_item)
     
    show screen gameUI
    "Test"