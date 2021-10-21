
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
            xmaximum 300
            spacing 10
            label "Character Details" xalign 0.5
            label "Level: [pc.level]"
            label "HP: [pc.hp]/[pc.max_hp]"
            label "MP: [pc.mp]/[pc.max_mp]"
            
        #inventory grid

        grid 10 7:
            yalign 0.5
            spacing 5
            for item in inventory:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_item", item)
            for i in range(len(inventory), 70):
                frame:
                    style "slot"

        #item details
        vbox:
            spacing 10
            label "Current Item" xalign 0.5
            
            if selected_item != None:
                frame:
                    style "slot"
                    add selected_item.img
                
                label "Value: [selected_item.value]"
                
                if isinstance(selected_item, Consumable):
                    textbutton "Use" action Function(selected_item.use, pc)

                if not isinstance(selected_item, KeyItem):
                    textbutton "Discard" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item",None)]

    textbutton "Return":
        action Return()
        xalign 0.5
        yalign 0.95