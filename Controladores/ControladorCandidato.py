from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorCandidato():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoCandidato = Candidato(infoCandidato)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elCandidato = Candidato(self.repositorioCandidato.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioCandidato.delete(id)