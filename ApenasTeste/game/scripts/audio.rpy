
label AudioSelect:

    scene Musica

    menu Audio:
        "Opções de musica"
        "Musica1":
            play music "audio/Music1.mp3"
        "Musica2":
            play music "audio/Music2.mp3"

        

screen BackAudio:
    hbox:
        xalign 0.5
        yalign 1.0
        textbutton _("Voltar") action Rollback()