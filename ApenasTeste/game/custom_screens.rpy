screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/botao.png"
        action ShowMenu("StatsUI")

screen StatsUI:
    add "images/background.png"
    frame:
        xalign 0.5
        yalign 0.5
        xoffset 30
        yoffset 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Knowledge" size 40
                text "Charm" size 40
                text "Guts" size 40
                text "Kindness" size 40
                text "Proficiency" size 40
            
            vbox:
                spacing 10
                text "[knowledge]" size 40
                text "[charm]" size 40
                text "[guts]" size 40
                text "[kindness]" size 40
                text "[proficiency]" size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto = "images/retorno_%s.png"
        action Return()