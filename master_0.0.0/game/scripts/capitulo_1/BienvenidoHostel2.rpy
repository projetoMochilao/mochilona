label BienvenidoHostel2:

    $hour = 15
    $minutes = 30

    " Chegando no hostel, Iara subiu direto para seu quarto, pegou uma troca de roupas e foi direto para o banheiro tomar um banho."

    "Após alguns minutos, Iara sai do banheiro."

    "toca o som de uma notificação e Iara puxa o telefone, Penélope enviou uma mensagem"

    "Conversa no Zap"

    Penelope "{i}Eae{/i}"

    Penelope "{i}Quer fazer alguma coisa?{/i}"

    Iara "{i}Claro{/i}"

    Penelope "{i}Nice{/i}"

    Penelope "{i}Onde vc ta?{/i}"

    Iara "{i}Eu estou ficando no Bienvenido Hostel{/i}"

    Penelope "{i}ok{/i}"

    Penelope "{i}já to indo){/i}"

    "Iara desce para o saguão, e se senta no lobby, após alguns minutos Penélope chega no hostel."

    Penelope "Eae, bem, tem um shopping aqui perto que é bem legal, mas dá tempo de irmos em outro lugar antes."

    Penelope "Eu sei de dois aqui por perto, o Monumento a la historia de México e o El Crucero Park, onde você quer ir?"

    menu:
        "Monumento a la historia de México":
            jump IndoAoMonumento
        "El Crucero Park":
            jump IndoAoPark
