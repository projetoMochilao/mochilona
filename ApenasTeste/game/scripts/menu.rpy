
screen menu:
    imagemap:
        ground "images/Prancheta1.png"
        #hover - imagem quando o mause esta por cima

        hotspot(349,79,229,189) action Return("inventario")
        hotspot(765,81,230,188) action Return("lembrancas")
        hotspot(350,386,232,188) action Return("musica")
        hotspot(769,388,227,189) action Return("menu")
    
screen mapa:
    imagemap:
        ground "images/Mapa/Botoes.png"
        #hover - imagem quando o mause esta por cima

        hotspot(669,254,52,50) action Return("Brasil")
        hotspot(471,248,53,56) action Return("Chile")
        hotspot(563,421,53,53) action Return("Argentina")


