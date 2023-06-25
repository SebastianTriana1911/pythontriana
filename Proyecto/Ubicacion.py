class Ubicacion:
    def __init__ (self,codigoDepartamento,codigoMunicipio,nombreDepartamento,nombreMunicipio):
        self.__codigoDepartamento = codigoDepartamento
        self.__codigoMunicipio = codigoMunicipio
        self.__nombreDepartamento = nombreDepartamento
        self.__nombreMunicipio = nombreMunicipio

    def getDatosUbicacion (self):
        return f"""Los datos de la ubicacion son:
        Codigo de departamento: {self.__codigoDepartamento}
        Codigo de municipio: {self.__codigoMunicipio}
        Nombre de departamento: {self.__nombreDepartamento}
        Nombre de municipio: {self.__nombreMunicipio}"""