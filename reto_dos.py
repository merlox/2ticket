# -*- coding: utf-8 -*-
# Desarrolla un programa que:
#     1. Genere 1_000_000 identificadores aleatorios.
#     2. Genere 3 bloques de identificadores de forma aleatoria usando los
#         tickets anteriores y donde cada bloque contenga un número aleatorio de
#         eventos que suponga entre un 50% y un 75% de los identificadores. Estos
#     3 bloques de identificadores se considerarán como los que son conocidos
#         por cada nodo por lo que un bloque puede contener valores que están en
#         otro.
#     3. A partir exclusivamente de estos 3 bloques, el programa mostrará por
#         pantalla:
#         a. La cantidad de tickets comunes en A, B y C.
#         b. El ticket común a A, B y C con el identificador más bajo.
#         c. El ticket común a A, B y C con el identificador más alto.

from base58 import b58encode
from random import randint

estado = ('v', 'u')

class Event_Manager:
    events = []
    ticket_counter = 11111 # Empieza en 11111 según los requisitos del programa

    # Crea un identificador y lo añade a la lista de identificadores
    def create_identifier(self):
        identifier = b58encode(str(randint(1e9, 9999999999)))
        return identifier

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

# Al comenzar, crear una instancia del event manager y crear 1 millon de identificadores
def start():
    event_manager = Event_Manager()
    identifiers = []
    for i in range(1000000):
        identifiers.append(event_manager.create_identifier())

start()
