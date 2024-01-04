#Karime Itzel Ruvalcaba Pérez A01656188

def buscando_reflexion(relacion):
    elementos=set()
    for par in relacion:
        elementos.add(par[0])
        elementos.add(par[1])

    for elemento in elementos:
        if (elemento,elemento) not in relacion:
            return " no reflexiva"
    return "reflexiva"

#def buscando_simetria(relacion):
    
      
def main():
    
    relacion={(0,0),(0,1),(0,3),(1,0),(1,1),(2,2),(3,0),(3,3)}

    reflexiva=buscando_reflexion(relacion)
    #symetrica=buscando_simetria(relacion)
    #transitiva=buscando_transicion(relacion)

    print(f"La relacion es: {reflexiva}")

if __name__ == '__main__':
    main()

