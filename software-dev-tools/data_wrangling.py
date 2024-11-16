import pandas as pd

def clean(datos):
    return datos.dropna()

class Limpiador():

    nombre = 'sin nombre'
    datos = None

    def __init__(self, nombre_personalizado, datos_personalizados):
        self.nombre = nombre_personalizado
        self.datos = datos_personalizados
    
    def clean(self):
        return self.datos.dropna()

if __name__ == '__main__':
    print('Esta es una libreria de limpieza de datos!')