from Ocupacion import *
from Ubicacion import *
class Vacante ():
    def __init__ (self,numVacantes,salario,experienciaMeses,tipoContrato,jornadaLaboral,tipoSalario,ocupacion,ubicacion):
        self.__numVacantes = numVacantes
        self.__salario = salario
        self.__experienciaMeses = experienciaMeses
        self.__tipoContrato = tipoContrato
        self.__jornadaLaboral = jornadaLaboral
        self.__tipoSalario = tipoSalario
        self.__ocupacion = ocupacion
        self.__ubicacion = ubicacion

    def getDatosVacantes (self):
        return f"""Los datos de la vacante son:
        Ocupacion: {self.__ocupacion}
        Numero de vacantes: {self.__numVacantes}
        Salario: {self.__salario}
        Experiencia en meses: {self.__experienciaMeses}
        Tipo de contrato: {self.__tipoContrato}
        Ubicacion: {self.__ubicacion}
        Jornada laboral: {self.__jornadaLaboral}
        Tipo de salario: {self.__tipoSalario} """