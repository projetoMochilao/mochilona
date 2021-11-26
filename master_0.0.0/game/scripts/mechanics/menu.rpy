
screen menu_screen:
    style_prefix "menu"

    add "images/menu/MapaMundi.png"

    hbox:
        ymaximum 720
        yminimum 720
        vbox:
            yalign 0.05
            xmaximum 640
            xminimum 640
            spacing 10

    vbox:
        xalign 0.1
        yalign 0.5
        textbutton _("História") action ShowMenu('history')
        textbutton _("Salvar") action ShowMenu('save')
        textbutton _("Preferências") action ShowMenu('preferences')
        textbutton _("Salvar rápido") action QuickSave()
        textbutton _("Carregar rápido") action QuickLoad()



    textbutton "Diario":
        action ShowMenu("daily_screen1")
        xalign 0.1
        yalign 0.1
    
        
    

    text "{color=ffffff}{size=+20}[days]/[months]/[year] - [hour]:[minutes]{/size}{/color}":
        xalign 0.95 
        yalign 0.95

    image "images/Capitulo1/Characters/Iara_waving1.png":
        xalign 0.5 
        yalign 0.35
        zoom 1.2
    

    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95

