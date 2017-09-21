class NodoArbolAVL(object):

    def __init__(self, d):
        self.dato=d
        self.fe=0
        self.raiz = None
        self.hijoIzquierdo = None
        self.hijoDerecho = None


    def vernodo(self):
        return self.dato


class ArbolAVL(object):

    def __init__(self):
        self.raiz=None


    def buscar(self,d,r):
        if self.raiz ==None:
            return  None
        elif r.dato ==d:
            return r
        elif r.dato<d:
            return self.buscar(d,r.hijoDerecho)
        else:
            return self.buscar(d, r.hijoIzquierdo)

    def obtenerFE(self, x):
        if x==None:
            return -1
        else:
            return x.fe


    def rotacionIzquierda(self, c):
        auxiliar = c.hijoIzquierdo
        c.hijoIzquierdo = auxiliar.hijoDerecho
        auxiliar.hijoDerecho =c
        c.fe = max(self.obtenerFE(c.hijoIzquierdo),self.obtenerFE(c.hijoDerecho))+1
        auxiliar.fe = max(self.obtenerFE(auxiliar.hijoIzquierdo),self.obtenerFE(auxiliar.hijoDerecho))+1
        return auxiliar

    def rotacionDerecha(self, c):
        auxiliar = c.hijoDerecho
        c.hijoDerecho = auxiliar.hijoIzquierdo
        auxiliar.hijoIzquierdo = c
        c.fe = max(self.obtenerFE(c.hijoIzquierdo), self.obtenerFE(c.hijoDerecho)) + 1
        auxiliar.fe = max(self.obtenerFE(auxiliar.hijoIzquierdo), self.obtenerFE(auxiliar.hijoDerecho)) + 1
        return auxiliar

    def rotacionDobleIzquierda(self, c):
        c.hijoIzquierdo= self.rotacionDerecha(c.hijoIzquierdo)
        temporal = self.rotacionIzquierda(c)
        return  temporal

    def rotacionDobleDerecha(self, c):
        c.hijoDerecho = self.rotacionIzquierda(c.hijoDerecho)
        temporal = self.rotacionDerecha(c)
        return temporal

    def insertarAVL(self, nuevo,subAr):
        nuevoPadre = subAr
        if nuevo.dato<subAr.dato:
            if subAr.hijoIzquierdo ==None:
                subAr.hijoIzquierdo =nuevo
            else:
                subAr.hijoIzquierdo = self.insertarAVL(nuevo,subAr.hijoIzquierdo)
                if self.obtenerFE(subAr.hijoIzqueirdo) - self.obtenerFE(subAr.hijoDrecho) == 2:
                    if nuevo.dato < subAr.hijoIzquierdo.dato:
                        nuevoPadre = self.rotacionIzquierda(subAr)
                    else:
                        nuevoPadre = self.rotacionDobleIzquierda(subAr)


        elif nuevo.dato > subAr.dato:
            if subAr.hijoDerecho ==None:
                subAr.hijoDerecho = nuevo
            else:
                subAr.hijoDerecho = self.insertarAVL(nuevo,subAr.hijoDerecho)
                if self.obtenerFE(subAr.hijoDerecho)- self.obtenerFE(subAr.hijoIzquierdo)==2:
                    if nuevo.dato > subAr.hijoDerecho.dato:
                        nuevoPadre = self.rotacionDerecha(subAr)
                    else:
                        nuevoPadre= self.rotacionDobleDerecha(subAr)



        else:
            print "nodo duplicado"

         #actualizando altura

        if subAr.hijoIzquierdo == None and subAr.hijoDerecho !=None:
            subAr.fe =subAr.hijoDerecho.fe+1

        elif subAr.hijoDercho==None and subAr.hijoIzquierdo !=None:
            subAr.fe = subAr.hijoIzquierdo.fe+1

        else:
            subAr.fe = max(self.obtenerFE(subAr.hijoIzquierdo),self.obtenerFE(subAr.hijoDerecho))+1

        return nuevoPadre



    def insertar(self,d):
            nuevo = NodoArbolAVL(d)

            if self.raiz==None:
                self.raiz = nuevo;
            else:
                self.raiz = self.insertar(nuevo,self.raiz)

    def inOrden(self, r):
        if r != None:
            self.inOrden(r.hijoIzquierdo)
            print (r.dato + ",")
            self.inOrden(r.hijoDerecho)

    def preOrden(self, r):
        if r != None:
            print (r.dato + ",")
            self.preOrden(r.hijoIzquierdo)
            self.preOrden(r.hijoDerecho)

    def postOrden(self, r):
        if r != None:
            self.postOrden(r.hijoIzquierdo)
            self.postOrden(r.hijoDerecho)
            print (r.dato + ",")





