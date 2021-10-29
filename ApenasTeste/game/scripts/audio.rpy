
label AudioSelect:

    scene Musica

    menu Audio:
        "Opções de musica"
        "Musica1":
            play music "audio/Music1.mp3"
            renpy.get_return_stack()
            
        "Musica2":
            play music "audio/Music2.mp3"
            renpy.get_return_stack()

