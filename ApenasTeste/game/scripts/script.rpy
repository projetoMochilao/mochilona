
define e = Character("Eileen")

# parte_inventário

default inventory = []
default listMusic = []
default selected_item = None
default pc = Player(7, 5, 5, 1)

default arma1_item = Consumable("arma1", 50, 100, 0)
default arma2_item = Consumable("arma2", 50, 100, 0)
default arma3_item = Consumable("arma3", 50, 100, 0)
default faca_item = KeyItem("faca")
default escudo_item = KeyItem("escudo")
default espada_item = KeyItem("espada")

image bg paisagem1 = "images/Mapa/background1.jpg"
image bg paisagem2 = "images/Mapa/background2.jpg"
image bg paisagem3 = "images/Mapa/background3.jpg"
image bg paisagem4 = "images/Mapa/background4.jpg"


label start:
    scene america1
    show screen relogio

    # parte_inventário
    $inventory.append(arma1_item)
    $inventory.append(arma2_item)
    $inventory.append(arma3_item)
    $inventory.append(faca_item)
    $inventory.append(escudo_item)
    $inventory.append(espada_item)
     
    show screen gameUI
    "Test"

    call screen mapa

    if _return == "Brasil":
        jump cena1
    
    elif _return == "Chile":
        jump cena2

    elif _return == "Argentina":
        jump cena3


    
label cena1:
    scene ruas
    "Brasil"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena4

label cena2:
    scene ruas
    "Chile"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena5

label cena3:
    scene ruas
    "Argentina"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena6

label cena4:
    scene bg paisagem1
    "TESTE - CENA 4"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena7

label cena5:
    scene bg paisagem2
    "TESTE - CENA 5"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena7

label cena6:
    scene bg paisagem3
    "TESTE - CENA 6"
    $minutos += 15
    if (minutos >= 60):
            $minutos -= 60
            $horas += 1
            if (horas >= 24):
                $horas = 0
    jump cena7

label cena7:
    scene bg paisagem4
    "TESTE - CENA 7"
    


screen mapa:
    imagemap:
        ground "images/Mapa/Botoes.png"
        #hover - imagem quando o mause esta por cima

        hotspot(669,254,52,50) action Return("Brasil")
        hotspot(471,248,53,56) action Return("Chile")
        hotspot(563,421,53,53) action Return("Argentina")
