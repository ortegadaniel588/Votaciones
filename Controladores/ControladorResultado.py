from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los Resultados")

    def create(self, elPartido):
        print("Crear un Resultado")

    def show(self, id):
        print("Mostrando un Resultado con id ", id)

    def update(self, id, elPartido):
        print("Actualizando Resultado con id", id)

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
