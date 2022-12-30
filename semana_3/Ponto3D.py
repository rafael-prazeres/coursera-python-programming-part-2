class Ponto3D:

    def __init__(self, x = 0, y = 0, z = 0):
        self.put(x, y, z)

    def __str__(self):
        return "(%d, %d, %d)"%(self.x, self.y, self.z)

    def get(self):
        return self.x, self.y, self.z

    def put(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = x, y, z

    def distancia_origem(self):
        origem = Ponto3D()
        d = self.distancia(origem)
        return d

    def distancia(self, other):
        d = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
        return d

    def ponto_medio(self, other):
        return Ponto3D((self.x + other.x)/2, (self.y + other.y)/2, (self.z + other.z)/2)
