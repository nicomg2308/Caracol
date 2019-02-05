import Logicaas lb

def main():
    m = lb.txtToArray(open("recorrido.txt").read())
    print(lb.imprimirCar(m,0,0))

if __name__ == "__main__":
    main()
