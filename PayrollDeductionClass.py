class PayrollDeduction:

    def __init__(self, descr, date, charge_amt, empID):
        self.__descr = descr
        self.__date = date
        self.__charge_amt = charge_amt
        self.__empID = empID

    def set_descr(self, descr):
        self.__descr = descr

    def get_descr(self):
        return self.__descr

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_charge_amt(self, charge_amt):
        self.__charge_amt = charge_amt

    def get_charge_amt(self):
        return self.__charge_amt

    def set_empID(self, empID):
        self.__empID = empID

    def get_empID(self):
        return self.__empID