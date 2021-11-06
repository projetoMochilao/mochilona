init python:

    daily_thing = [
        "Pagina 1",
        "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "Pagina 2",
        "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "Pagina 3",
        "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "Pagina 4",
        "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        ]
    daily_index = 0

    def PlusIndex():
        if daily_index != 6:
            daily_index + 2

    def LessIndex():
        if daily_index != 0:
            daily_index - 2




screen daily_screen1:


    add "bg daily"

    hbox:

        vbox:
            textbutton "Pagina1":
                action ToggleScreen("daily_screen1")
            textbutton "Pagina2":
                action ToggleScreen("daily_screen2")
            textbutton "Pagina3":
                action ToggleScreen("daily_screen3")
            textbutton "Pagina4":
                action ToggleScreen("daily_screen4")
            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            text daily_thing[0] align (0.5, 0.5) xpos 320 ypos 90
        
        vbox:
            xmaximum 400
            xminimum 400
            text daily_thing[1] align (0.5, 0.5) xpos 250 ypos 300
        
                
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
                action ToggleScreen("daily_screen1")
            textbutton "Pagina2":
                action ToggleScreen("daily_screen2")
            textbutton "Pagina3":
                action ToggleScreen("daily_screen3")
            textbutton "Pagina4":
                action ToggleScreen("daily_screen4")

        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            text daily_thing[2] align (0.5, 0.5) xpos 320 ypos 90
        
        vbox:
            xmaximum 400
            xminimum 400
            text daily_thing[3] align (0.5, 0.5) xpos 250 ypos 300
    
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95
        
                
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
                action ToggleScreen("daily_screen1")
            textbutton "Pagina2":
                action ToggleScreen("daily_screen2")
            textbutton "Pagina3":
                action ToggleScreen("daily_screen3")
            textbutton "Pagina4":
                action ToggleScreen("daily_screen4")

            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            text daily_thing[4] align (0.5, 0.5) xpos 320 ypos 90
        
        vbox:
            xmaximum 400
            xminimum 400
            text daily_thing[5] align (0.5, 0.5) xpos 250 ypos 300
        
                
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95






screen daily_screen4:


    add "bg daily"

    hbox:

        vbox:
            textbutton "Pagina1":
                action ToggleScreen("daily_screen1")
            textbutton "Pagina2":
                action ToggleScreen("daily_screen2")
            textbutton "Pagina3":
                action ToggleScreen("daily_screen3")
            textbutton "Pagina4":
                action ToggleScreen("daily_screen4")

            
        vbox:
            xmaximum 550
            xminimum 550
            spacing 20
            text daily_thing[6] align (0.5, 0.5) xpos 320 ypos 90
        
        vbox:
            xmaximum 400
            xminimum 400
            text daily_thing[7] align (0.5, 0.5) xpos 250 ypos 300
        
                
    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95