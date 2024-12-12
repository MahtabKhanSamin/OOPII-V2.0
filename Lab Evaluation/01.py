from abc import ABC,abstractmethod

class NegativeError(Exception):
    pass

class Student(ABC):
    def __init__(self,a,b,c):
        self._StudentID=a
        self._Name=b
        self._TuitionFee=c
    def getID(self):
        return self._StudentID
    def getName(self):
        return self._Name
    def getTuition(self):
        return self._TuitionFee
    @abstractmethod
    def CalculateFee(self):
        pass

class Undergraduate(Student):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.__CreditHour=d
    def getCredit(self):
        return self.__CreditHour
    def setCredit(self,a):
        self.__CreditHour=a
    def CalculateFee(self):
        self._TuitionFee=self.__CreditHour*150

class Graduate(Student):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.__researchclass=d
    def getResearch(self):
        return self.__researchclass
    def setResearch(self,a):
        self.__researchclass=a
    def CalculateFee(self):
        self._TuitionFee=self.__researchclass*3000
try:
    Un = Undergraduate(1608, "Mahtab Khan", 10000, 30)
    Un.CalculateFee()
    Gra = Graduate(1951, "Sadman Sakib", 10000, 15)
    Gra.CalculateFee()
    if Gra.getTuition() < 0 or Un.getTuition() < 0:
        raise NegativeError
except:
    print("Negative Found")
    print("Please Enter ")

else:
    print(Un.getID())
    print(Un.getName())
    print(Un.getCredit())
    print(Un.getTuition())

    print(Gra.getID())
    print(Gra.getName())
    print(Gra.getResearch())
    print(Gra.getTuition())


