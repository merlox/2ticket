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
    tickets_sold = []
    attendants = []
    ticket_counter = 1
    last_position = 1

    # Crea un identificador y lo añade a la lista de identificadores
    def create_ticket_tuple(self):
        (ticket_id, ticket_counter) = (b58encode(str(randint(1e9, 9999999999))), self.ticket_counter)
        ticket_tuple = (ticket_id, ticket_counter)
        self.tickets_sold.append(ticket_tuple)
        self.ticket_counter += 1
        return ticket_tuple

    # Crea un asistente al evento y lo devuelve
    def create_attendant(self):
        (ticket_id, position) = (b58encode(str(randint(1e9, 9999999999))), self.last_position)
        attendant_tuple = (ticket_id, position)
        self.attendants.append(attendant_tuple)
        self.last_position += 1
        return attendant_tuple

# Al comenzar, crear una instancia del event manager y crear 1 millon de identificadores
def start():
    event_manager = Event_Manager()
    aforo = 50

    # 1. Genere 75 tickets formados por 2-tuplas <id-ticket, numeración>.
    print("Creando 75 tickets...")
    for i in range(75):
        (ticket_id, ticket_counter) = event_manager.create_ticket_tuple()
        print("Ticket id {}, ticket counter {}".format(ticket_id, ticket_counter))

    # 2. Genere 65 asistentes caracterizados por 2-tuplas <id-ticket, posición-en-cola-de-entrada>.
    print("\nCreando 65 asistentes...")
    for i in range(65):
        (ticket_id, position) = event_manager.create_attendant()
        print("Ticket id {}, posicion en la cola {}".format(ticket_id, position))

start()
