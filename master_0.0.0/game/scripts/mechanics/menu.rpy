style slot:
    background Frame("squere",0.0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

screen menu_screen:
    style_prefix "menu"

    add "images/menu/MapaMundi.png"

    hbox:
        ymaximum 720
        yminimum 720
        vbox:
            
            xmaximum 640
            xminimum 640
            spacing 7

            # Atributos
            label "Iara Rodrigues" xalign 0.5
            label "Atributo1 [pc.atb1]/[pc.max_atb1]" xalign 0.3
            label "Atributo2 [pc.atb2]/[pc.max_atb2]" xalign 0.3
            label "Atributo2 [pc.atb3]/[pc.max_atb3]" xalign 0.3
            label "Atributo3 [pc.atb4]/[pc.max_atb4]" xalign 0.3

            # Inventário

            for item in inventory:
                textbutton "- [item.img]" action SetVariable("selected_item", item) xalign 0.3
            
            vbox:
                xalign 0.3
                spacing 10
                label "Item" xalign 0.5

                if selected_item != None:
                    frame:
                        style "slot"
                        add selected_item.img
                    
                    label "[selected_item.img]"

                    if selected_item.value != 0:
                        label "Valor [selected_item.value]"
                    
                    if isinstance(selected_item, Consumable):
                        textbutton "Usar" action Function(selected_item.use, pc)
                    
                    if not isinstance(selected_item, KeyItem):
                        textbutton "Descartar" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)]

    vbox:
        xalign 0.80
        yalign 0.5
        textbutton _("História") action ShowMenu('history')
        textbutton _("Salvar") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Preferências") action ShowMenu('preferences')



    textbutton "Diario":
        action ShowMenu("daily_screen1")
        xalign 0.8
        yalign 0.1
    
        
    

    text "{color=#ff0}{size=+20}[days]/[months]/[year] - [hour]:[minutes]{/size}{/color}" xalign 0.95 yalign 0.95

    

    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95

