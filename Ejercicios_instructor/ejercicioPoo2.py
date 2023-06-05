class Curso():
    def __init__ (self):
        self.__curso = []
        
    def ingCurso (self,curso):
        self.__curso += [curso]
        
    def getCursos (self):
        return self.__curso
    
    def busCursos (self,curso1):
        self. curso1 = curso1
        for i in (self.__curso):
            if curso1 == i:
                return f"{curso1} si esta en la lista"
        else:
            return f"{curso1} no se encuentra en la lista"
        
    def elimCurso (self,curso2):
        self.curso2 = curso2
        for i in (self.__curso):
            if curso2 == i:
                return self.__curso.remove(curso2)
        else:
            return f"{curso2} no se remover de la lista por que no existe dicho curso"
        
    # def modCurso (self,cursoBuscar,cursoNUevo):
        # self.cursoBuscar = cursoBuscar
        # self.cursoNUevo = cursoNUevo
        # for i in (self.__curso):
            # if self.__curso[i] == cursoBuscar:
                # cursoBuscar == cursoNUevo
                # cursoBuscar == self.__curso[i]
                # return self.__curso
        # else:
            # return f"{cursoNUevo} no se modificart el curso de la lista por que no existe dicho curso"
        
        
        
p = Curso()
p.ingCurso("primero")
p.ingCurso("segundo")
p.ingCurso("tercero")
p.ingCurso("cuarto")
p.ingCurso("quinto")
print (p.getCursos())
print(p.busCursos("primero"))
print(p.elimCurso("tercero"))
print(p.getCursos())
#print(p.modCurso("segundo", "seg"))

