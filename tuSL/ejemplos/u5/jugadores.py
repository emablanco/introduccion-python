# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:05:26 2016

@author: emiliano
"""

from datetime import date
import dateutil

class Jugador():
    """Clase Jugador"""
    def __init__(self, nombre=None, fecha_nac=None, posicion=None):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.posicion = posicion
        self.clubes = []
        
    def agregar_club(self, club):
        '''agrega club a la lista de clubes'''
        self.clubes.append(club)
    
    def club_actual(self):
        '''retorna último club'''
        return self.clubes[-1]

    def calcular_edad(self):
        '''retorna la edad del jugador'''
        d, m, a = self.fecha_nac.split("-")
        fecha_nac = date(int(a), int(m), int(d))
        edad = dateutil.relativedelta.relativedelta(date.today(), fecha_nac)
        return edad.years
    
    def __str__(self):
        salida = self.nombre
        salida += '\n' + '='*len(self.nombre) + '\n'
        salida += 'Edad: ' + str(self.calcular_edad()) + '\n'
        salida += 'Posición: ' + self.posicion + '\n'
        return salida
        
    def __lt__(self, otro):
        '''retorna True si self es menor a otro'''
        return (self.calcular_edad() > otro.calcular_edad())
