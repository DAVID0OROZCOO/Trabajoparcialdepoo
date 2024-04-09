# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:23:31 2024

@author: USUARIO
"""

class Cliente:
    def __init__(self, cedula: int, nombre: str, direccion: str, telefono: int):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono


class Videojuego:
    def __init__(self, nombre_juego: str, codigo_juego: int, precio_alquiler: int, precio_venta: int):
        self.nombre_juego = nombre_juego
        self.codigo_juego = codigo_juego
        self.precio_alquiler = precio_alquiler
        self.precio_venta = precio_venta


class Tienda:
    def __init__(self):
        self.listaclientes: dict[int, Cliente] = dict()
        self.catalogo: dict[int, Videojuego] = dict()

    def registrar_cliente(self, cedula: int, nombre: str, direccion: str, telefono: int):
        if self.buscar_cliente(cedula) is None:
            cliente = Cliente(cedula, nombre, direccion, telefono)
            self.listaclientes[cedula] = cliente
            print("Cliente registrado con éxito.")
        else:
            print("El cliente ya está registrado en la tienda.")

    def buscar_cliente(self, cedula: int):
        return self.listaclientes.get(cedula)

    def buscar_juego_por_nombre(self, nombre_juego: str):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                return juego
        return None
