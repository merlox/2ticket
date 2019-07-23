# -*- coding: utf-8 -*-
# Desarrolla un programa que:
#     1. Genere 75 tickets formados por 2-tuplas <id-ticket, numeración>.
#     2. Genere 65 asistentes caracterizados por 2-tuplas <id-ticket,
#         posición-en-cola-de-entrada>.
#         a. 10 personas de las que adquirieron tickets no se han personado al
#             evento, por tanto tenemos 75 tickets vendidos, 65 asistentes y un
#             aforo de 50 personas.
#         b. El id-ticket del asistente siempre estará contenido entre los 75
#             tickets vendidos.
#         c. Ante un mismo id-ticket, sólo puede cumplirse que
#             numeración=posición-en-cola-de-entrada en caso de azar.
#     3. Implemente un algoritmo lo más justo posible para gestionar la entrada
#         al evento hasta completar el aforo, mostrando por pantalla aquellos
#         valores que consideres oportunos para ilustrar el proceso llevado a cabo.

from base58 import b58encode, b58decode
from random import randint, shuffle
from copy import deepcopy

estado = ('v', 'u')

# Clase que se encarga de crear eventos y métodos para ambos elementos
class Event_Manager:
    events = []
    ticket_counter = 11111 # Empieza en 11111 según los requisitos del programa

    # Crea un identificador y lo añade a la lista de identificadores
    def create_ticket_tuple(self):
        ticket_tuple = (b58encode(str(randint(1e9, 9999999999))), self.ticket_counter)
        self.ticket_counter += 1
        return ticket_tuple

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

# Clase de eventos individuales para crear nuevos eventos conteniendo tickets
class Event:
    tickets = []

    def __init__(self, tickets):
        self.tickets = tickets

# Clase de tickets para almacenar y crear nuevos tickets individuales
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

    # 1. Genere 75 tickets formados por 2-tuplas <id-ticket, numeración>.
    print("Creando 75 tickets...")
    for i in range(75):
        (ticket_id, ticket_counter) = event_manager.create_ticket_tuple()
        print("Ticket id {}, ticket counter {}".format(ticket_id, ticket_counter))

    # 2. Genere 65 asistentes caracterizados por 2-tuplas <id-ticket, posición-en-cola-de-entrada>.
    print("Creando 65 tickets...")
    for i in range(65):
        (ticket_id, ticket_counter) = event_manager.create_ticket_tuple()
        print("Ticket id {}, ticket counter {}".format(ticket_id, ticket_counter))


start()
