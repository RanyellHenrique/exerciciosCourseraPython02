class Triangulo:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b != self.c and self.a != self.c:
            return 'escaleno'
        return 'isóceles'
    
    def retangulo(self): 
        if self.a**2 == self.b**2 + self.c**2 or self.b**2 == self.a**2 + self.c**2 or self.c**2 == self.a**2 + self.b**2:
            return True
        return False

    def semelhantes(self, t2):
        tri1 = [self.a, self.b, self.c]
        tri2 = [t2.a, t2.b, t2.c]
        tri2.sort()
        tri1.sort()
        if (tri1[0] / tri2[0]) == (tri1[1] / tri2[1]) == (tri1[2] / tri2[2]) and (tri1[0] / tri2[0]) == (tri1[2] / tri2[2]):
            return True
        return False
