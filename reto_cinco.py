# -*- coding: utf-8 -*-
# Implementación de una DLT en python como proof-of-concept de funcionamiento

from base58 import b58encode
from hashlib import sha256
from time import time
from json import dumps
from random import randint

class Bloque:
    bloque = {
        'id': 0,
        'timestamp': 0,
        'hash_anterior': 0,
        'tickets_json': [],
        'hash_actual': 0,
    }

    def __init__(self, id, hash_anterior, tickets_json):
        self.bloque['id'] = id
        self.bloque['timestamp'] = time()
        self.bloque['hash_anterior'] = hash_anterior
        self.bloque['tickets_json'] = tickets_json
        self.bloque['hash_actual'] = self.generar_hash()

    def generar_hash(self):
        return sha256(dumps(self.bloque, sort_keys=True).encode('utf-8')).hexdigest()

class Tickets_Manager:
    tickets = []
    ticket_counter = 11111 # Empieza en 11111 según los requisitos del programa

    # Crea la cantidad especificada de tickets y los añade al array de tickets
    def create_ticket(self):
        estado_numero = randint(0, 1)
        ticket = Ticket(
            b58encode(str(randint(1e9, 9999999999))),
            b58encode(str(self.ticket_counter)),
            randint(1, 1e5),
            'v' if estado_numero == 0 else 'u'
        )
        self.tickets.append(ticket)
        self.ticket_counter += 1
        return ticket

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

def start():
    ticket_manager = Tickets_Manager()
    ticket_1 = ticket_manager.create_ticket()
    ticket_2 = ticket_manager.create_ticket()
    tickets_json = [ticket_1, ticket_2]

    primer_bloque = {
        'hash_anterior': 0,
        'tickets_json': [],
    }
    # Hashea el primer bloque
    genesis_hashed = sha256(dumps(primer_bloque, sort_keys=True).encode('utf-8')).hexdigest()

    bloque = Bloque(
        1,
        genesis_hashed,
        tickets_json,
    )
    print(bloque)
    # print('{} {} {} {} {}'.format(bloque.id, bloque.timestamp, bloque.hash_anterior, bloque.tickets_json, bloque.hash_actual))

start()
