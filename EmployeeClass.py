class Employee:

    def __init__(self, name, idnum, depar, jt, msalary):
        self.__name = name
        self.__idnum = idnum
        self.__depar = depar
        self.__jt = jt
        self.__msalary = msalary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_idnum(self, idnum):
        self.__idnum = idnum

    def get_idnum(self):
        return self.__idnum

    def set_depar(self, depar):
        self.__depar = depar

    def get_depar(self):
        return self.__depar

    def set_jt(self, jt):
        self.__jt = jt

    def get_jt(self):
        return self.__jt

    def set_msalary(self, msalary):
        self.__msalary = msalary

    def get_msalary(self):
        return self.__msalary
