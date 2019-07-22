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

from base58 import b58encode, b58decode
from random import randint, shuffle
from copy import deepcopy

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
    blocks = []

    print("Creando 1 millon de identificadores...")
    for i in range(1000000):
        identifiers.append(event_manager.create_identifier())
    print("Hecho")

    # Creamos 3 bloques con ese millon de identificadores
    for i in range(3):
        identifiers_copy = deepcopy(identifiers) # Necesitamos una copia para poder alterar el order de los bloques
        block_percent = randint(5e5, 7.5e5)
        # Hacemos un shuffle para seleccionar elementos aleatorios
        shuffle(identifiers_copy)
        # Añadimos el array con el porcentaje de elementos en el bloque
        blocks.append(identifiers_copy[:block_percent])

    # Buscamos los elementos comunes en esos 3 bloques comparando los bloques
    # a. La cantidad de tickets comunes en A, B y C.
    repeated = list(set(blocks[0]) & set(blocks[1]) & set(blocks[2]))
    print("Identificadores repetidos en los tres bloques {}".format(len(repeated)))

    repeated_integers = []
    # b. El ticket común a A, B y C con el identificador más bajo.
    # c. El ticket común a A, B y C con el identificador más alto.
    # Para encontrar el valor más bajo, es inevitable tener que convertir cada base58 a int de nuevo
    for i, item in enumerate(repeated):
        repeated_integers.append(b58decode(item))

    print("numero comun con el identificador mas bajo: {}".format(min(repeated_integers)))
    print("numero comun con el identificador mas alto: {}".format(max(repeated_integers)))

start()
