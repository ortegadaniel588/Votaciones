from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado


class ControladorResultado():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioResultado.findAll()

    def create(self, infoResultado):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoResultado = Resultado(infoResultado)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elResultado = Resultado(self.repositorioResultado.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elResultado.__dict__

    def update(self, id, infoResultado):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        resultadoActual = Resultado(self.repositorioResultado.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        resultadoActual.id = infoResultado["id"]
        resultadoActual.numero_mesa = infoResultado["numero_mesa"]
        resultadoActual.id_partido = infoResultado["id_partido"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioResultado.delete(id)