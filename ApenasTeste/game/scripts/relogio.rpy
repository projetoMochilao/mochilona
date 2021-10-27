init python:
    horas = 9
    minutos = 15

    screen relogio:
        text "{color=#ff0}{size=+20}[horas] : [minutos]{/size}{/color}" xalign 0.02 yalign 0.05

    def AddTime(valorMinutos):
        minutos += valorMinutos
        if minutos >= 60:
            minutos -= 60
            horas ++
        if horas >= 24:
            horas = 0