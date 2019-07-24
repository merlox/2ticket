# -*- coding: utf-8 -*-
# Implementación de una DLT en python como proof-of-concept de funcionamiento

from base58 import b58encode
from hashlib import sha256
from time import time
from json import dumps
from random import randint
from pprint import pprint

class Blockchain:
    bloques = []
    nodo = ''
    hash_mas_reciente = 0

    # Crea el primer bloque y lo añade al hash mas reciente
    def __init__(self):
        primer_bloque = self.create_block([])
        # Hashea el primer bloque
        bloque_hashed = sha256(dumps(primer_bloque, sort_keys=True).encode('utf-8')).hexdigest()
        self.hash_mas_reciente = bloque_hashed

    def create_block(self, tickets_json):
        bloque = Bloque(
            1,
            self.hash_mas_reciente,
            tickets_json,
        )
        self.bloques.append(bloque)
        hash_mas_reciente = bloque.generar_hash()
        return bloque.bloque

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
        self.bloque['timestamp'] = int(time())
        self.bloque['hash_anterior'] = hash_anterior
        self.bloque['tickets_json'] = dumps(tickets_json, sort_keys=True).encode('utf-8')
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
        return ticket.ticket

# Clase de tickets para almacenar y crear nuevos tickets individuales
class Ticket:
    ticket = {
        'id_ticket': 0,
        'id_evento': 0,
        'numero_entrada': 0,
        'estado': None,
    }

    def __init__(self, id_ticket, id_evento, numero_entrada, estado):
        self.ticket['id_ticket'] = id_ticket
        self.ticket['id_evento'] = id_evento
        self.ticket['numero_entrada'] = numero_entrada
        self.ticket['estado'] = estado


def start():
    ticket_manager = Tickets_Manager()
    blockchain = Blockchain()
    ticket_1 = ticket_manager.create_ticket()
    ticket_2 = ticket_manager.create_ticket()
    tickets_json = [ticket_1, ticket_2]

    pprint(blockchain.create_block(tickets_json))
    # print('{} {} {} {} {}'.format(bloque.id, bloque.timestamp, bloque.hash_anterior, bloque.tickets_json, bloque.hash_actual))

start()
