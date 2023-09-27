from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los Partidos")

    def create(self, elPartido):
        print("Crear un Partido")

    def show(self, id):
        print("Mostrando un Partido con id ", id)

    def update(self, id, elPartido):
        print("Actualizando Partido con id", id)

    def delete(self, id):
        print("Elimiando Partido con id ", id)
