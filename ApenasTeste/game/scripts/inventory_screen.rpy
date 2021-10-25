
style inventory_label:
    xalign 0.2

style slot:
    background Frame("squere",0.0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

screen inventory_screen:
    style_prefix "inventory"

    add "white"
    hbox:
        #character details
        vbox:
            xmaximum 400
            xminimum 400
            spacing 10
            label "Caracteristicas" xalign 0.5
            label "Level: [pc.level]"
            label "HP: [pc.hp]/[pc.max_hp]"
            label "MP: [pc.mp]/[pc.max_mp]"
            
        #inventory grid

#        grid 10 7:
#            yalign 0.5
#            spacing 5
#            for item in inventory:
#                frame:
#                    style "slot"
#                    imagebutton idle item.img action SetVariable("selected_item", item)
#            for i in range(len(inventory), 70):
#                frame:
#                    style "slot" 

        vbox:
            xmaximum 500
            xminimum 500
            spacing 5
            for item in inventory:
                textbutton "- [item.img]" action SetVariable("selected_item", item)

        #item details
        vbox:
            spacing 10
            label "Item" xalign 0.5
            
            if selected_item != None:
                frame:
                    style "slot"
                    add selected_item.img
                
                label "[selected_item.img]"

                if selected_item.value != 0:
                    label "Valor: [selected_item.value]"
                
                if isinstance(selected_item, Consumable):
                    textbutton "Usar" action Function(selected_item.use, pc)

                if not isinstance(selected_item, KeyItem):
                    textbutton "Descartar" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item",None)]

    textbutton "Retornar":
        action Return()
        xalign 0.5
        yalign 0.95