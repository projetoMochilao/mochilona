init python:

    daily_thing = [
        "Willian",
        "18",
        "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        ]
    daily_index = 0





screen daily_screen1:


    add "bg daily"

    hbox:

        vbox:
            textbutton "Pagina1":
                action ShowMenu("daily_screen1")
            textbutton "Pagina2":
                action ShowMenu("daily_screen2")
            textbutton "Pagina3":
                action ShowMenu("daily_screen3")
            textbutton "Pagina4":
                action ShowMenu("daily_screen4")

            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            label "Pagina 1" xalign 0.5 yalign 0.5
        
        vbox:
            xmaximum 500
            xminimum 500
            label "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." xalign 0.5 yalign 0.5
        
                
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95

#    imagebutton:
#        action Rollback()
#        xalign 0.05
#        yalign 0.5
#        idle "images/diario/leftArrow.png"
    
#    imagebutton:
#        action ShowMenu("daily_screen2")
#        xalign 0.95
#        yalign 0.5
#        idle "images/diario/rightArrow.png"

        







screen daily_screen2:

    add "bg daily"

    hbox:
        vbox:
            textbutton "Pagina1":
                action ShowMenu("daily_screen1")
            textbutton "Pagina1":
                action ShowMenu("daily_screen2")
            textbutton "Pagina1":
                action ShowMenu("daily_screen3")
            textbutton "Pagina1":
                action ShowMenu("daily_screen4")

        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            label "Pagina 2" xalign 0.5
        
        vbox:
            xmaximum 400
            xminimum 400
            label "ir since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.":
                xalign 0.5 
                yalign 0.5
        
                
#    textbutton "Retornar":
#        action Rollback()
#        xalign 0.5
#        yalign 0.95
    
#    imagebutton:
#        action ShowMenu("daily_screen1")
#        xalign 0.05
#        yalign 0.5
#        idle "images/diario/leftArrow.png"




screen daily_screen3:


    add "bg daily"

    hbox:

        vbox:
            textbutton "Pagina1":
                action ShowMenu("daily_screen1")
            textbutton "Pagina2":
                action ShowMenu("daily_screen2")
            textbutton "Pagina3":
                action ShowMenu("daily_screen3")
            textbutton "Pagina4":
                action ShowMenu("daily_screen4")

            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            label "Pagina 3" xalign 0.5 yalign 0.5
        
        vbox:
            xmaximum 500
            xminimum 500
            label "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." xalign 0.5 yalign 0.5
        
                
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95






screen daily_screen4:


    add "bg daily"

    hbox:

        vbox:
            textbutton "Pagina1":
                action ShowMenu("daily_screen1")
            textbutton "Pagina2":
                action ShowMenu("daily_screen2")
            textbutton "Pagina3":
                action ShowMenu("daily_screen3")
            textbutton "Pagina4":
                action ShowMenu("daily_screen4")

            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            label "Pagina 4" xalign 0.5 yalign 0.5
        
        vbox:
            xmaximum 500
            xminimum 500
            label "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." xalign 0.5 yalign 0.5
        
                
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95