def palindromo(palabra):
    b=list(palabra.replace(" ",""))
    #a,b=list(palabra.replace(" ","")), list(palabra.replace(" ","")) 
    b.reverse()
    return list(palabra.replace(" ","")) == b
    #return a == b
if __name__ == "__main__":
    print("Ingrese frase")
    palabra=input()
    print(palindromo(palabra))