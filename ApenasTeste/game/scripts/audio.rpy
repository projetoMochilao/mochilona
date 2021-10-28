init python:

    class AudioPlay:
        def __init__(self, name, file):
            self.name = name
            self.file = file

screen audio_screen:
    style_prefix "listAudio"

    add "white"
    hbox:

        vbox:
            xmaximum 500
            xminimum 500
            spacing 5
            text "Lista de Musicas:"
            for som in listMusic:
                textbutton "- [som.name]" action SetVariable("selected_item", som)
        

    imagemap:
            ground "images/Mapa/Botoes.png"
            #hover - imagem quando o mause esta por cima

            hotspot(669,254,52,50) action Return("play")
    
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95

if _return == "play":
    play music "selected_item.file"



                

    