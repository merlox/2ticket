# -*- coding: utf-8 -*-
# Implementación de una DLT en python como proof-of-concept de funcionamiento

from base58 import b58encode
from hashlib import sha256
from time import time
from json import dumps, loads
from random import randint
from pprint import pprint
from copy import deepcopy

class Blockchain:
    bloques = []
    nodo = ''
    hash_mas_reciente = 0
    last_id = 0

    # Crea el primer bloque y lo añade al hash mas reciente
    def __init__(self):
        primer_bloque = self.create_block([])
        # Hashea el primer bloque
        bloque_hashed = sha256(dumps(primer_bloque, sort_keys=True).encode('utf-8')).hexdigest()
        self.hash_mas_reciente = bloque_hashed

    def create_block(self, tickets_json):
        bloque = Bloque(
            self.last_id,
            self.hash_mas_reciente,
            tickets_json,
        )
        self.last_id += 1
        bloque_copy = deepcopy(bloque.bloque)
        self.bloques.append(bloque_copy)
        hash_mas_reciente = bloque.generar_hash()
        return bloque_copy

    def get_tickets_from_blocks(self):
        tickets = []
        for bloque in self.bloques:
            ticket_in_block = loads(bloque['tickets_json'])
            for ticket in ticket_in_block:
                tickets.append(ticket)
        return tickets

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

# La blockchain funciona creando bloques con tickets nuevos y los usuarios se
# intercambian los tickets mediante p2p
def start():
    ticket_manager = Tickets_Manager()
    blockchain = Blockchain()
    tickets = []

    while True:
        opcion_seleccionada = leer_input()
        if opcion_seleccionada == 1:
            ticket = ticket_manager.create_ticket()
            tickets.append(ticket)
            print('')
            pprint(ticket)
            print('')
        elif opcion_seleccionada == 2:
            bloque = blockchain.create_block(tickets)
            tickets = []
            print('')
            pprint(bloque)
            print('')
        elif opcion_seleccionada == 3:
            print('')
            pprint(blockchain.get_tickets_from_blocks())
            print('')
        elif opcion_seleccionada == 4:
            print('')
            pprint(blockchain.bloques)
            print('')
        elif opcion_seleccionada == 5:
            exit()
        else:
            print("Error, introduce una opcion valida")

def leer_input():
    print("Selecciona una opcion para interactuar con la blockchain")
    print("\t1) Crear ticket")
    print("\t2) Crear bloque con los tickets existentes")
    print("\t3) Ver tickets almacenados en la blockchain")
    print("\t4) Ver bloques")
    print("\t5) Salir")
    return input()

start()
