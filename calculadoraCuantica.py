import math


class Complejo:
    def __init__(self, n1: float, n2: float, isCartesiano=True):
        """
        :param n1: parte real o el valor de rho
        :param n2: parte compleja o el valor del angulo en grados
        :param isCartesiano: especifica si es cartesiano o no
        self.__real
        self.__complejo
        self.__modulo
        self.__angle
        """

        if isCartesiano:
            self.real = n1
            self.complejo = n2
            self.modulo = self.__calculateModulo()
            self.angle = self.__calculateAngle()
            self.rho = self.modulo
        else:
            self.rho = n1
            self.angle = n2
            self.real = self.rho*math.cos(self.angle*math.pi/180)
            self.complejo = self.rho * math.sin(self.angle * math.pi / 180)
            self.modulo = self.__calculateModulo()

    @staticmethod
    def decode(num: str):
        """
        :param num: es de la forma a +bi
        :return:
        """
        aux = num.split()
        if 'i' in aux[1]:
            return Complejo(int(aux[0].strip()), int(aux[1][:len(aux[1])-1].strip()))
        else:
            return Complejo(int(aux[1].strip()), int(aux[0][:len(aux[0]) - 1].strip()))

    def getCartesiano(self):
        return "({0}, {1})".format(round(self.real, 2), round(self.complejo,2))

    def get(self):
        return "{0} {1}i".format(self.real, self.__getComplejo())

    def getPolar(self):
        return "({0}, {1}°)".format(self.rho, self.angle)

    def getAngle(self):
        return "{0}°".format(self.angle)

    def __getComplejo(self):
        if self.complejo > 0:
            return '+{0}'.format(self.complejo)
        else:
            return str(self.complejo)

    def __calculateAngle(self):
        if self.real != 0:
            num = round(math.atan2(self.complejo, self.real)*57.3, 2)
            if self.complejo < 0:
                if self.real < 0:
                    num += 180
                elif self.real > 0:
                    num = 360 - num
            return num
        else:
            return None

    def __calculateModulo(self):
        return ((self.real ** 2) + (self.complejo ** 2)) ** 0.5


def sumComplex(n1: Complejo, n2: Complejo) -> Complejo:
    return Complejo(n1.real + n2.real, n1.complejo + n2.complejo)


def restComplex(n1: Complejo, n2: Complejo) -> Complejo:
    return Complejo(n1.real - n2.real, n1.complejo - n2.complejo)


def multComplex(n1: Complejo, n2: Complejo) -> Complejo:
    real = (n1.real * n2.real) + (n1.complejo * n2.complejo * -1)
    decimal = (n1.real * n2.complejo) + (n1.complejo * n2.real)
    return Complejo(real, decimal)


def divComplex(n1: Complejo, n2: Complejo) -> Complejo or None:
    denominador = (n2.real**2) + (n2.complejo**2)
    if denominador != 0:
        real = ((n1.real*n2.real) + (n1.complejo*n2.complejo))/denominador
        complejo = ((n2.real*n1.complejo) - (n1.real*n2.complejo))/denominador
        return Complejo(real, complejo)
    else:
        return None


def toPolar(a: Complejo):
    return a.getPolar()
    pass


def toCartesianas(a: Complejo):
    return a.getCartesiano()


def conjugado(a: Complejo) -> Complejo:
    return Complejo(a.real, a.complejo*-1)


def getFase(a: Complejo):
    return round(a.angle, 2)


def multMatrices(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C
