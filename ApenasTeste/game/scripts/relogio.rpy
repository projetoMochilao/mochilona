init python:
    horas = 9
    minutos = 15
    days = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]
    day = 0

    def AddTime(valorMinutos):
            minutos += valorMinutos
            if minutos >= 60:
                minutos -= 60
                horas += 1
                if horas >= 24:
                    horas = 0



screen relogio:
    text "{color=#ff0}{size=+20}[horas] : [minutos]{/size}{/color}" xalign 0.02 yalign 0.05

    