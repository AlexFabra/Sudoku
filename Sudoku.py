import math
class Sudoku:
    # guardem els números necessaris per que una fila, columna o quadrant estiguin complets:
    nombresNecessaris = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #creem el constructor de Sudoku. Li passarem com a paràmetre un array d'arrays:
    def __init__(self,arrays):
        self.arrays=arrays
    #el métode actualitza actualitza arrays, posant el número introduït a les coordenades:
    def actualitza(self,nouNumero,cX,cY):
        self.arrays[cX][cY]=nouNumero
    #Donats els paràmetres cX i nouNumero, el mètode comprovar fila serveix
    # per analitzar si l'últim número introduït és repeteix.
    #cX és la coordenadaX, és a dir, la fila que volem obtenir.
    #nouNumero és el número introduït per l'usuari.
    def comprovarFila(self,fila,nouNumero):
        numerosFila = []
        for nColumna in range(len(self.arrays)):
            numerosFila.append(arrays[fila][nColumna])
        #si al vector hi ha més d'un valor igual al nouNumero, retorna false
        #false representa un error en el Sudoku:
        if numerosFila.count(nouNumero)>1:
            print("Aquest número ja hi és a la fila.")
            return False
        else:
            return True

    #funció que donat el número a comprovar i la fila on comprovar la seva repetició, retorna true si no s'ha repetit.
    #columna és la columna que volem obtenir.
    #nouNumero és el número que volem veure si es repeteix.
    def comprovarColumna(self,columna,nouNumero):
        numerosColumna = []
        for nFila in range(len(self.arrays)):
            numerosColumna.append(arrays[nFila][columna])
        #si al vector hi ha més d'un valor igual al nouNumero, retorna false
        #false representa un error en el Sudoku:
        if numerosColumna.count(nouNumero)>1:
            print("Aquest número ja hi és a la columna.")
            return False
        else:
            return True

    #funció que donat un número a comprovar i la posició horitzontal i vertical on s'ubica, identifica el cuadrant
    #i retorna false si ja hi ha un número igual en aquest:
    def comprovarQuadrant(self,columna,fila,nouNumero):
        #vector on guardarem els nombres del quadrant:
        numQuadrant = []

        # Com que volem trobar el primer número del quadrant per iterar fins a l'últim, treiem el floor de la divisió
        # de les coordenades entre 3 (això ens donarà un numero del 0 al 2) i ho multipliquem per 3, que en donarà el
        # numero inicial d'un quadrant:
        fila = (math.floor(fila / 3)*3)
        columna = (math.floor(columna / 3)*3)

        #   Amb el iterador posem els numeros del quadrant a la llista:
        for num in range(fila, fila + 3):
            #extend afegeix al final de la llista 'numQuadrant' el valor de la coordenada de 'arrays':
            #guardem els valors de tres en tres:
            numQuadrant.extend(arrays[num][columna:columna + 3])

        #si al vector hi ha més d'un valor igual al nouNumero, retorna false
        #false representa un error en el Sudoku:
        if numQuadrant.count(nouNumero)>1:
            print("Aquest número ja hi és al quadrant.")
            return False
        else:
            return True

    #finalFila comprova que la fila estigui complerta i retorna true només en aquest cas:
    def finalFila(self,fila):
        numerosFila = []
        for nColumna in range(len(self.arrays)):
            numerosFila.append(arrays[fila][nColumna])
        #mirem si els valors de la llista nombresNecessaris hi son a numerosFila:
        comprovacio = all(item in numerosFila for item in self.nombresNecessaris)
        return comprovacio

    #finalColumna comprova que la columna estigui complerta i retorna true només en aquest cas:
    def finalColumna(self,columna):
        numerosColumna = []
        for nFila in range(len(self.arrays)):
            numerosColumna.append(arrays[nFila][columna])
        #mirem si els valors de la llista nombresNecessaris hi son a numerosColumna:
        comprovacio = all(item in numerosColumna for item in self.nombresNecessaris)
        return comprovacio

    #finalQuadrant comprova que el quadrant estigui complert i retorna true només en aquest cas:
    def finalQuadrant(self,fila,columna):
        #aquest codi és reutilitzat de la funció comprovarQuadrant i està comentat allà:
        numerosQuadrant = []
        fila = (math.floor(fila / 3)*3)
        columna = (math.floor(columna / 3)*3)
        for num in range(fila, fila + 3):
            numerosQuadrant.extend(arrays[num][columna:columna + 3])
        #mirem si els valors de la llista nombresNecessaris hi son a numerosQuadrant:
        comprovacio = all(item in numerosQuadrant for item in self.nombresNecessaris)
        return comprovacio

    def sudokuComplert(self):
        completat = True
        comptador=0
        comptador1=0
        while completat and comptador<9:
            completat=self.finalFila(comptador)
            if completat:
                completat=self.finalColumna(comptador)
            comptador+=1
            while completat and comptador1<9:
                completat=self.finalQuadrant(comptador,comptador1)
                comptador1+=1
        return completat

    # creem el métode toString que retorna l'estat de l'objecte:
    def __str__(self):
        mostraString=""
        contador=0
        contador1=0
        mostraString += "\n-------------------------------\n"
        #fem un for anidat per recòrrer el vector de vectors:
        for y in arrays:
            for x in y:
                if(contador%3==0):
                    mostraString+="|"
                #guardem a mostraString el valor:
                mostraString+=" "+ str(x)+ " "
                contador += 1
            mostraString += "|"
            contador1+=1
            #si el modul del contador1 entre 3 equival a 0:
            if (contador1 % 3 == 0):
                #fem un salt de línea quan sortim del for intern:
                mostraString+="\n-------------------------------\n"
            else:
                mostraString += "\n"
            #tornem a posar el contador a 1:
            contador=0
        #retornem el string que és el sudoku:
        return(mostraString)


#declarem l'array que tractarem com a sudoku:
arrays = \
[[3, 1, 5, 6, 2, 9, 8, 4, 7],
[7, 0, 6, 1, 0, 8, 0, 0, 0],
[8, 3, 1, 4, 7, 9, 2, 6, 5],
[5, 0, 3, 0, 0, 5, 0, 7, 0],
[6, 8, 7, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 7, 0, 0, 6, 0, 0],
[4, 7, 9, 5, 8, 0, 0, 2, 0],
[1, 0, 0, 4, 3, 0, 5, 0, 9],
[9, 0, 8, 9, 0, 0, 0, 0, 6]]

#fem un objecte passant-li 'arrays' com a paràmetre:
s1 = Sudoku(arrays)
#declarem el boolean sudokuComplert en valor false:
sudokuComplert=False

while sudokuComplert==False:
    #mostrem el sudoku (#imprimim el vector de vectors amb format gràcies al __str__):
    print(s1)
    #declarem l'String coordenada:
    coordenada = "0,0"
    #demanem les coordenades a modificar:
    coordenada=input("introdueïx coordenada ([fila],[columna]): ")
    #demanem un valor per posar en les coordenades:
    nouValor=int(input("introdueïx nou valor: "))
    #dividim l'String 'coordenada' per la coma per treballar amb els valors
    coo=coordenada.split(',')
    #fem un cast a integer i guardem els valors:
    x=int(coo[0])
    y=int(coo[1])
    #restem els valors perque 1 sigui la primera fila o columna, i no la segona:
    x=x-1
    y=y-1
    #executem la funció 'actualitza()'
    s1.actualitza(nouValor,x,y)
    #si cap d'aquest mètodes retorna false, és que es repeteix el valor en fila, columna o quadrant:
    filaValorRepetit=s1.comprovarFila(x,nouValor)
    columnaValorRepetit=s1.comprovarColumna(y,nouValor)
    quadrantValorRepetit=s1.comprovarQuadrant(x,y,nouValor)
    #si cap d'aquests mètodes retorna false, és que no estan complerts la fila, la columna o el quadrant:
    filaComplerta=s1.finalFila(x)
    columnaComplerta=s1.finalColumna(y)
    quadrantComplert=s1.finalQuadrant(x,y)
    #si la funció sudokuComplert() ens retorna false, és que el sudoku no està complert:
    sudokuComplert=s1.sudokuComplert()


