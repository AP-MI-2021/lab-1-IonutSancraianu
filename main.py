'''
Returneaza true daca n este prim si false daca nu
n - nr. intreg
returneaza True daca nr. este prim sau False daca numarul nu este prim
'''
def is_prime(n):
    if n<2 :
        return False
    else :
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
    return True

assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False

'''
Returneaza produsul numerelor din lista lst.
lst - lista cu numere intregi 
returneaza produsul numerelor din lista
'''
def get_product(lst):
    p = 1
    for i in lst:
        i=int(input("Scrieti numarul: "))
        p = p*i
    return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
Algortimul - scaderi repetate
x,y - numere intregi
returneaza - cel mai mare divizor comun
'''
def get_cmmdc_v1(x, y):
    if x==0 or y==0:
        return False
    while x!=y:
        if x<y:
            y=y-x
        else :
            x=x-y
    return x

assert get_cmmdc_v1(0,1) is False
assert get_cmmdc_v1(39,51)==3

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
Algoritmul lui Euclid
x,y - numere intregi
returneaza - cel mai mare divizor comun
'''
def get_cmmdc_v2(x , y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

assert get_cmmdc_v2(2,3)==1
assert get_cmmdc_v2(16,150)==2


def main():
    shouldRun=True
    while(shouldRun):
        print("Alegeti optiune 1, 2 sau 3 in functie de exercitiul ales"
              " sau x daca doriti sa iesiti")
        optiune=input("Scrieti optiunea: ")
        if optiune=="x":
            shouldRun=False
        if optiune=="1":
            n = int(input("Scrieti numarul pentru a verifica daca este prim:"))
            print(is_prime(n))
        if optiune == "2":
            lst = ["a", "b", "c", "d"]
            print("Produsul numerelor din lista este: ",get_product(lst))
        if optiune=="3":
            alg=input("Scrieti <eu> daca vreti sa folositi algoritmul 2 "
                      "sau <sc> daca vreti sa folositi algoritmul 1: ")
            if alg == "eu":
                x = int(input("Primul numar este: "))
                y = int(input("Al doilea numar este: "))
                print("Cel mai mic divizor comun este",get_cmmdc_v2(x,y))
            elif alg == "sc":
                x = int(input("Primul numar este: "))
                y = int(input("Al doilea numar este: "))
                print("Cel mai mic divizor comun este ",get_cmmdc_v1(x, y))


if __name__ == '__main__':
  main()