init python:
    cs_stats_list = []
    cs_stats_selected = None

    class CSCharacterStat:
        def __init__(self, img, name, btName, desc, cha, int, str, dex):
            self.img = img
            self.name = name
            self.desc = desc
            self.cha = cha
            self.int = int
            self.str = str
            self.dex = dex
            self.btName = btName

    def _csSelectStatsOf(stat):
        global cs_stats_selected
        cs_stats_selected = stat

    def csCharacterStatAdd(img, name, btName, desc, cha, int, str, dex):
        global cs_stats_list
        vNewStat = CSCharacterStat(img, name, btName, desc, cha, int, str, dex)
        canAdd = True
        for item in cs_stats_list:
            if item.btName == btName:
                canAdd = False
        if canAdd:
            if(not cs_stats_list):
                _csSelectStatsOf(vNewStat)
            cs_stats_list.append(vNewStat)

style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 5

screen cs_stats:
    add "/stats-menu/background.png"
    text "Personagens" size 32 xpos 122 ypos 62 align (0.5, 0.5)
    vbox:
        xpos 8
        ypos 120
        spacing 5
        for stat in cs_stats_list:
            imagebutton:
                idle "/stats-menu/" + stat.btName + "-idle.png"
                hover "/stats-menu/" + stat.btName + "-hover.png"
                selected_idle "/stats-menu/" + stat.btName + "-hover.png"
                selected_hover "/stats-menu/" + stat.btName + "-hover.png"
                xalign 0.5
                action [Function(_csSelectStatsOf, stat), SelectedIf(cs_stats_selected and cs_stats_selected.btName == stat.btName)]

    imagebutton:
        xpos 8
        ypos 630
        idle "/stats-menu/back-idle.png"
        hover "/stats-menu/back-hover.png"
        selected_idle "/stats-menu/back-idle.png"
        selected_hover "/stats-menu/back-hover.png"
        action Return(None)

    
    text "Descrição" size 32 xpos 620 ypos 185 align (0.5, 0.5)

    if cs_stats_selected != None:
        hbox:
            xpos 350
            ypos 60
            spacing 30
            vbox:
                text "Carisma: [cs_stats_selected.cha]" xalign 1.0 size 24
                text "Inteligencia: [cs_stats_selected.int]" xalign 1.0 size 24
            vbox:
                text "Força: [cs_stats_selected.str]" xalign 1.0 size 24
                text "Destreza: [cs_stats_selected.dex]" xalign 1.0 size 24
        text cs_stats_selected.name size 52 xpos 834 ypos 36
        text cs_stats_selected.desc size 20 xpos 285 ypos 246 xmaximum 665 first_indent 20
        add cs_stats_selected.img xanchor 0.5 yanchor 1.0 xpos 1120 ypos 680
    add "/stats-menu/foreground.png"
