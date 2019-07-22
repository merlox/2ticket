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

estado = ('v', 'u')

class Event_Manager:
    events = []
    ticket_counter = 11111 # Empieza en 11111 según los requisitos del programa

    # Crea la cantidad especificada de tickets y los añade al array de tickets
    def create_ticket(self):
        ticket = Ticket(
            b58encode(str(randint(1e9, 9999999999))),
            b58encode(str(self.ticket_counter)),
            randint(1, 1e5),
            estado[randint(0, 1)]
        )
        self.ticket_counter += 1
        print("Id ticket {}, Id evento {}, Numero {}, Estado {}".format(ticket.id_ticket, ticket.id_evento, ticket.numero_entrada, ticket.estado))

    # Crea la cantidad especificada de eventos y le añade tickets para cada uno entre 2 y 10 tickets
    def create_event(self):
        # Primero decidimos la cantidad de tickets a crear para el evento
        tickets_to_create = randint(2, 10)
        print('Creating event with {} tickets'.format(tickets_to_create))
        my_tickets = []
        for i in range(tickets_to_create):
            my_tickets.append(self.create_ticket())

        # Despues creamos el evento y añadimos los tickets
        self.events.append(Event(my_tickets))

class Event:
    tickets = []

    def __init__(self, tickets):
        self.tickets = tickets

class Ticket:
    id_ticket = 0
    id_evento = 0
    numero_entrada = 0
    estado = None

    def __init__(self, id_ticket, id_evento, numero_entrada, estado):
        self.id_ticket = id_ticket
        self.id_evento = id_evento
        self.numero_entrada = numero_entrada
        self.estado = estado

# Al comenzar, crear una instancia del event manager y crear 10 eventos
def start():
    event_manager = Event_Manager()
    for i in range(10):
        event_manager.create_event()

start()
