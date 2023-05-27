from django import template
from datetime import date, datetime

register = template.Library()

@register.filter #deixando assim, o nome do filtro fica com o mesmo nome da função
def mostra_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        dias = (value1 - value2).days
        texto = 'Dias'
        if dias == 1:
            texto = 'Dia'

        return f"{dias} {texto}."
    
    return "Ainda não foi devolvido."