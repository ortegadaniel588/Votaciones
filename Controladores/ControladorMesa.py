from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos los Mesas")

    def create(self, elMesa):
        print("Crear un Mesa")

    def show(self, id):
        print("Mostrando un Mesa con id ", id)

    def update(self, id, elMesa):
        print("Actualizando Mesa con id", id)

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
