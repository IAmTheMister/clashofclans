import csv

class Nodo:
    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.tipo, self.x, self.y))

class Mapa:
    def __init__(self, px, py, ox, oy, x, y, muros):
        self.px = px
        self.py = py
        self.ox = ox
        self.oy = oy
        self.x = x
        self.y = y
        self.muros = muros
        self.mapa = self.crear_mapa()
        self.distman = abs(self.ox - self.px) + abs(self.oy - self.py) 

    def __repr__(self):
        return str((self.px,self.py, self.ox, self.oy, self.x, self.y, self.muros))

    def crear_mapa(self):
        mapa = []
        for j in range(self.y):
            fila = []
            for i in range(self.x):
                if j == self.py and i == self.px:
                    fila.append("P")
                elif j == self.oy and i == self.ox:
                    fila.append("O")
                elif (i, j) in self.muros:
                    fila.append("M")
                else:
                    fila.append("x")
            mapa.append(fila)
        return mapa
    
    def heuristica(self):
        h = abs(self.ox - self.px) + abs(self.oy - self.py) 
        if (self.px, self.py) in self.muros:
            h += 100000

        return h
        

class Juego:
    def main(self):
        mapa = Mapa(3,0,1,4,5,5,[(1,2),(2,1)])
        for fila in mapa.mapa:
            print(fila)
        print("")
        mapa_exp = self.expandir_nodos(mapa)
        while mapa_exp.px != mapa_exp.ox or mapa_exp.py != mapa_exp.oy:
            mapa_exp = self.expandir_nodos(mapa_exp)


    def expandir_nodos(self, mapa):
        lista = []
        if mapa.px + 1 < mapa.x:
            mapa_2 = Mapa(mapa.px + 1, mapa.py, mapa.ox, mapa.oy, mapa.x, mapa.y, mapa.muros)
            lista.append(mapa_2)
        if mapa.py + 1 < mapa.y:
            mapa_2 = Mapa(mapa.px, mapa.py + 1, mapa.ox, mapa.oy, mapa.x, mapa.y, mapa.muros)
            lista.append(mapa_2)
        if mapa.px - 1 > 0:
            mapa_2 = Mapa(mapa.px - 1, mapa.py, mapa.ox, mapa.oy, mapa.x, mapa.y, mapa.muros)
            lista.append(mapa_2)
        if mapa.py - 1 > 0:
            mapa_2 = Mapa(mapa.px, mapa.py - 1, mapa.ox, mapa.oy, mapa.x, mapa.y, mapa.muros)
            lista.append(mapa_2)

        minimo_h = min(lista, key = lambda minimo:minimo.heuristica())
        for fila in minimo_h.mapa:
            print(fila)
        print("")
        return minimo_h

    def rep_mapa(self, archivo_mapa):
        px, py, ox, oy, x, y = 0, 0, 0, 0, 0, 0
        lista_mapa = []
        muros = []
        with open(archivo_mapa, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                lista_mapa.append(row)

        for fila in range(len(lista_mapa)):
            y = len(lista_mapa) - 1
            for col in range(len(lista_mapa[fila])):
                x = len(lista_mapa[col]) - 1
                if lista_mapa[fila][col] == "P":
                    py = fila
                    px = col
                elif lista_mapa[fila][col] == "O":
                    oy = fila
                    ox = col
                elif lista_mapa[fila][col] == "M":
                    muros.append((col,fila))

        # for fila in lista_mapa:
        #     print(fila)

        return Mapa(px, py, ox, oy, x, y, muros), lista_mapa

juego = Juego()
juego.main()