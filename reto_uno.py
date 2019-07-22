# -*- coding: utf-8 -*-
# - Que los ids de los tickets no sean secuenciales.
# - Que los ids de evento sean secuenciales siendo el primero el 11111.
# - Cada evento tenga entre 2 y 10 tickets emitidos.
# - Cada evento tenga tickets válidos y usados.

# - id-ticket: Identificador único y global del ticket en la
# infraestructura. Su valor es un texto en Base58 de longitud 10.
# 1
# - id-evento: Identificador único del evento. Su valor es un texto en
# Base58 de longitud 5.
# - número-de-entrada: Número de entrada para el evento. Su valor es un
# entero en el rango [1, 1_000_000].
# - estado: Estado del ticket. Su valor es un carácter en el dominio {v, u}.
# (v: válido, u: usado).

from base58 import b58encode
from random import randint

tickets = []
estado = ('v', 'u')
ticket_counter = 11111

# Crea la cantidad especificada de tickets y los añade al array de tickets
def crear_tickets(cantidad):
    global ticket_counter
    for i in range(cantidad):
        ticket = {
            "id_ticket": b58encode(str(randint(1e9, 9999999999))),
            "id_evento": b58encode(str(ticket_counter)),
            "numero_entrada": randint(1, 1e5),
            "estado": estado[randint(0, 1)]
        }
        ticket_counter += 1
        print("Id ticket {}, Id evento {}, Numero {}, Estado {}".format(ticket['id_ticket'], ticket['id_evento'], ticket['numero_entrada'], ticket['estado']))

crear_tickets(100)
